import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"


def get_users():
    response = requests.get(BASE_URL)
    response.raise_for_status()
    return response.json()


def put_user(user_id, data):
    response = requests.put(f"{BASE_URL}/{user_id}", json=data)
    response.raise_for_status()
    return response.json()


def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    response.raise_for_status()
    return response.status_code

def get_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    response.raise_for_status()
    return response.json()

def create_user(data):
    response = requests.post(BASE_URL, json=data)
    response.raise_for_status()
    return response.json()

def update_user(user_id, data):
    response = requests.put(f"{BASE_URL}/{user_id}", json=data)
    response.raise_for_status()
    return response.json()

def get_user_todos(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}/todos")
    response.raise_for_status()
    return response.json()
