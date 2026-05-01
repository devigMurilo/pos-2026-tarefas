from json import dump
from pathlib import Path
from xml.dom.minidom import parse


BASE_DIR = Path(__file__).parent


def texto(elemento, tag):
    no = elemento.getElementsByTagName(tag)[0]
    return no.firstChild.nodeValue.strip()


def textos(elemento, tag):
    return [
        no.firstChild.nodeValue.strip()
        for no in elemento.getElementsByTagName(tag)
        if no.firstChild
    ]


def converter_imovel(imovel):
    proprietario = imovel.getElementsByTagName("proprietario")[0]
    endereco = imovel.getElementsByTagName("endereco")[0]
    caracteristicas = imovel.getElementsByTagName("caracteristicas")[0]

    dados_proprietario = {
        "nome": texto(proprietario, "nome"),
    }

    emails = textos(proprietario, "email")
    telefones = textos(proprietario, "telefone")

    if emails:
        dados_proprietario["emails"] = emails

    if telefones:
        dados_proprietario["telefones"] = telefones

    dados_endereco = {
        "rua": texto(endereco, "rua"),
        "bairro": texto(endereco, "bairro"),
        "cidade": texto(endereco, "cidade"),
    }

    numeros = textos(endereco, "numero")
    if numeros:
        dados_endereco["numero"] = int(numeros[0])

    return {
        "descricao": texto(imovel, "descricao"),
        "proprietario": dados_proprietario,
        "endereco": dados_endereco,
        "caracteristicas": {
            "tamanho": float(texto(caracteristicas, "tamanho")),
            "numQuartos": int(texto(caracteristicas, "numQuartos")),
            "numBanheiros": int(texto(caracteristicas, "numBanheiros")),
        },
        "valor": texto(imovel, "valor"),
    }


dom = parse(str(BASE_DIR / "imobiliaria.xml"))
imoveis = dom.documentElement.getElementsByTagName("imovel")

dados = {
    "imobiliaria": {
        "imoveis": [converter_imovel(imovel) for imovel in imoveis]
    }
}

with open(BASE_DIR / "imobiliaria.json", "w", encoding="utf-8") as arquivo:
    dump(dados, arquivo, ensure_ascii=False, indent=2)
