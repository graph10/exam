from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import secrets
import requests
import json
from rest_framework_jwt.utils import jwt_encode_handler
from django.views.decorators.http import require_POST
import base64
import hashlib
from werkzeug.utils import secure_filename
from django.http import JsonResponse
import json
from django.utils import timezone
from datetime import timedelta
from django.utils.deprecation import MiddlewareMixin
from .middleware import SessionTimeoutMiddleware

def main(request):
    if 'user_id' in request.session:
        if 'last_activity' in request.session and \
           request.session.get_expiry() - timezone.now() > timedelta(days=7):
            return render(request, 'main/index_auth_complete.html')
        else:
            return render(request, 'main/index.html')
    else:
        return render(request, 'main/index.html')

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

            url = f"http://192.168.1.103:8000/reg?token={token}"
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

            url = f"http://192.168.1.103:8000/auth?token={token}"
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