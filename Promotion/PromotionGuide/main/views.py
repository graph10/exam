from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import secrets
import requests
import json
from rest_framework_jwt.utils import jwt_encode_handler
from django.views.decorators.http import require_POST
import base64
import hashlib
from werkzeug.utils import secure_filename
import json
from test_json import data
adr = "http://localhost:6969"
def main(request):
    if 'user_id' in request.session:
        urls = [
            {"type": "alc", "url": adr+"/getall"},
            {"type": "bitovuha", "url": adr+"/getall"},
            {"type": "candy", "url": adr+"/getall"},
            {"type": "coffee", "url": adr+"/getall"},
            {"type": "desert", "url": adr+"/getall"},
            {"type": "feed", "url": adr+"/getall"},
            {"type": "meat", "url": adr+"/getall"},
            {"type": "powder", "url": adr+"/getall"},
            {"type": "product", "url": adr+"/getall"}
        ]

        combined_data = []
        for item in urls:
            response = requests.get(item["url"], params={"type": item["type"]})
            # Предполагаем, что функция data принимает текст ответа и возвращает список словарей
            products = data(response.text)
            combined_data.extend(products)

        return render(request, 'main/index_auth_complete.html', {'combined_data': combined_data})
    else:
        urls = [
            {"type": "alc", "url": "http://192.168.1.100:6969/getall"},
            {"type": "bitovuha", "url": "http://192.168.1.100:6969/getall"},
            {"type": "candy", "url": "http://192.168.1.100:6969/getall"},
            {"type": "coffee", "url": "http://192.168.1.100:6969/getall"},
            {"type": "desert", "url": "http://192.168.1.100:6969/getall"},
            {"type": "feed", "url": "http://192.168.1.100:6969/getall"},
            {"type": "meat", "url": "http://192.168.1.100:6969/getall"},
            {"type": "powder", "url": "http://192.168.1.100:6969/getall"},
            {"type": "product", "url": "http://192.168.1.100:6969/getall"}
        ]

        combined_data = []
        for item in urls:
            response = requests.get(item["url"], params={"type": item["type"]})
            # Предполагаем, что функция data принимает текст ответа и возвращает список словарей
            products = data(response.text)
            combined_data.extend(products)

        return render(request, 'main/index.html', {'combined_data': combined_data})

def reg(request):
    if request.method == 'POST':
        if 'registration' in request.POST:
            def generate_jwt_token(login, password):
                header = {
                    'alg': 'HS256',
                    'typ': 'JWT'
                }
                payload = {
                    'login': login,
                    'password': password,
                    'exp': 600
                }
                header_encoded = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().strip('=')
                payload_encoded = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().strip('=')
                secret = '123456789'
                signature = hashlib.sha256(f'{header_encoded}.{payload_encoded}{secret}'.encode()).hexdigest()
                token = f'{header_encoded}.{payload_encoded}.{signature}'
                return token


            login = request.POST['login']
            password = request.POST['password']
            token = generate_jwt_token(login, password)

            url = adr + f"/reg?token={token}"
            response = requests.get(url)
            answer = response.text

            if answer == "успешная регистрация":
                request.session['user_id'] = secrets.token_hex(16)
                request.session['login'] = login
                request.session['password'] = password
                return render(request, 'main/index_auth_complete.html')
            if answer == "такой пользователь уже существует":
                text = "Такой пользователь уже зарегистрирован. Попробуйте войти в акканут или введите другие данные"
                return render(request, 'main/reg.html', {'text': text})
    else:
        return render(request, 'main/reg.html')

def auth(request):
    if request.method == 'POST':
        if 'auth' in request.POST:
            def generate_jwt_token(login, password):
                header = {
                    'alg': 'HS256',
                    'typ': 'JWT'
                }
                payload = {
                    'login': login,
                    'password': password,
                    'exp': 600
                }
                header_encoded = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().strip('=')
                payload_encoded = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().strip('=')
                secret = '123456789'
                signature = hashlib.sha256(f'{header_encoded}.{payload_encoded}{secret}'.encode()).hexdigest()
                token = f'{header_encoded}.{payload_encoded}.{signature}'
                return token


            login = request.POST['login']
            password = request.POST['password']
            token = generate_jwt_token(login, password)

            url = adr + f"/auth?token={token}"
            response = requests.get(url)
            answer = response.text

            if answer == "успешная авторизация":
                request.session['user_id'] = secrets.token_hex(16)
                request.session['login'] = login
                request.session['password'] = password
                return render(request, 'main/index_auth_complete.html')
            if answer == "неверный пароль":
                text = "Неверный пароль, попробуйте еще раз"
                return render(request, 'main/auth.html', {'text': text})
            if answer == "нет такого пользователя":
                text = "Такого пользователя не существует, попробуйте зарегистрироваться"
                return render(request, 'main/auth.html', {'text': text})
    else:
        return render(request, 'main/auth.html')

def account(request):
    return render(request, "main/account.html")

def postponed(request):
    return render(request, "main/postponed.html")
