import os
from datetime import datetime
from functools import wraps
from pathlib import Path
 
from flask.cli import load_dotenv
import requests
from flask import Flask, flash, redirect, render_template, request, session, url_for


load_dotenv()

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)

oauth.register(
    name="suap",
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    access_token_url="https://suap.ifrn.edu.br/o/token/",
    authorize_url="https://suap.ifrn.edu.br/o/authorize/",
    api_base_url="https://suap.ifrn.edu.br/api/v2/",
    client_kwargs={"scope": "read"},
)



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "access_token" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function

SUAP_API_URL = "https://suap.ifrn.edu.br/api"
SUAP_OAUTH_AUTHORIZE_URL = "https://suap.ifrn.edu.br/o/authorize/"
SUAP_OAUTH_TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"


def load_env():
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


load_env()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "troque-esta-chave-em-producao")
app.config["SUAP_OAUTH_CLIENT_ID"] = os.getenv("SUAP_OAUTH_CLIENT_ID", "")
app.config["SUAP_OAUTH_CLIENT_SECRET"] = os.getenv("SUAP_OAUTH_CLIENT_SECRET", "")
app.config["SUAP_OAUTH_REDIRECT_URI"] = os.getenv("SUAP_OAUTH_REDIRECT_URI", "")


def suap_request(method, path, token=None, **kwargs):
    headers = kwargs.pop("headers", {})
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.request(
        method,
        f"{SUAP_API_URL}{path}",
        headers=headers,
        timeout=20,
        **kwargs,
    )
    response.raise_for_status()
    return response.json()


def first_present(*values, default=""):
    for value in values:
        if value not in (None, ""):
            return value
    return default

def get_user_context():
    profile = session.get("profile") or {}
    student = session.get("student") or {}
    username = session.get("username", "")
    name = first_present(profile.get("nome"), student.get("nome"), username, default="Aluno")

    return {
        "name": name,
        "username": username,
        "email": first_present(profile.get("email"), student.get("email_academico"), student.get("email_escolar")),
    }


def fetch_user_data():
    token = session["access_token"]
    profile = suap_request("GET", "/rh/meus-dados/", token=token)
    student = suap_request("GET", "/ensino/meus-dados-aluno/", token=token)
    session["profile"] = profile
    session["student"] = student


def save_token_session(token_data, username=""):
    access_token = token_data.get("access") or token_data.get("access_token")
    refresh_token = token_data.get("refresh") or token_data.get("refresh_token")

    if not access_token:
        raise KeyError("access_token")

    session.clear()
    session["username"] = username or token_data.get("username", "")
    session["access_token"] = access_token
    session["refresh_token"] = refresh_token
    fetch_user_data()


def fetch_report_card(year, period):
    page = 1
    results = []
    payload = {"count": 0, "next": None, "previous": None, "results": []}

    while True:
        payload = suap_request(
            "GET",
            f"/ensino/meu-boletim/{year}/{period}/",
            token=session["access_token"],
            params={"page": page},
        )
        results.extend(payload.get("results", []))
        if not payload.get("next"):
            break
        page += 1

    payload["results"] = results
    return payload


@app.context_processor
def inject_user():
    return {
        "current_user": get_user_context() if "access_token" in session else None,
        "current_year": datetime.now().year,
    }


@app.template_filter("label")
def label(value):
    return str(value).replace("_", " ").title()


@app.template_filter("pretty")
def pretty(value):
    if value is True:
        return "Sim"
    if value is False:
        return "Nao"
    if value in (None, ""):
        return "-"
    return value


@app.route("/")
def index():
    if "access_token" in session:
        return redirect(url_for("profile"))
    return render_template(
        "index.html",
        oauth_enabled=bool(app.config["SUAP_OAUTH_CLIENT_ID"]),
    )


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if not username or not password:
        flash("Informe usuario e senha do SUAP.", "danger")
        return redirect(url_for("index"))

    try:
        token_data = suap_request(
            "POST",
            "/token/pair",
            json={"username": username, "password": password},
        )
        save_token_session(token_data, username=username)
        flash("Login realizado com sucesso.", "success")
        return redirect(url_for("profile"))
    except requests.HTTPError as error:
        status = error.response.status_code if error.response else "?"
        flash(f"Nao foi possivel autenticar no SUAP. Status {status}.", "danger")
    
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.clear()
    flash("Voce saiu da sessao.", "info")
    return redirect(url_for("index"))


@app.route("/perfil")
@login_required
def profile():
    try:
        if not session.get("profile") or not session.get("student"):
            fetch_user_data()
    except requests.RequestException:
        flash("Nao foi possivel atualizar seus dados agora.", "warning")

    return render_template(
        "profile.html",
        profile=session.get("profile", {}),
        student=session.get("student", {}),
    )


@app.route("/boletim")
@login_required
def report_card():
    year = request.args.get("ano", str(datetime.now().year), type=int)
    period = request.args.get("periodo", 1, type=int)
    years = list(range(datetime.now().year, datetime.now().year - 6, -1))
    boletim = {"count": 0, "results": []}

    try:
        boletim = fetch_report_card(year, period)
    except requests.HTTPError as error:
        status = error.response.status_code if error.response else "?"
        flash(f"Nao foi possivel carregar o boletim. Status {status}.", "danger")
    except requests.RequestException:
        flash("Nao foi possivel conectar ao SUAP para carregar o boletim.", "danger")

    return render_template(
        "boletim.html",
        boletim=boletim,
        selected_year=year,
        selected_period=period,
        years=years,
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False, use_reloader=False)
