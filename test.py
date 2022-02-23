import json

import requests
import os
import environ
import json

env = environ.Env()
environ.Env.read_env('.env')
host = os.environ.get("DJANGO_ALLOWED_HOSTS", '127.0.0.1').split(' ')[1]


def rest_api():
    data = {
    "user": {"username": "user",
    "email": "user@gmail.com",
    "password": "12345678"}
}
    response = requests.post(f'http://{host}:8000/auth/register/', json=data)
    login = requests.post(f'http://{host}:8000/auth/login/', json=data)
    user = json.loads(login.content).get('user', '')
    ticket = requests.post(f'http://{host}:8000/support/tickets/', data={"status": "solved"}, headers={'Authorization': f'Token {user.get("token")}'})
    assert response.status_code == 201
    assert login.status_code == 200
    assert ticket.status_code == 201
rest_api()
