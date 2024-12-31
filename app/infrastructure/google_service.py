import time

import requests


def get_tokens(client_id):

    device_auth_url = "https://oauth2.googleapis.com/device/code"

    # Запрос на авторизацию устройства
    payload = {
        "client_id": client_id,
        "scope": "https://www.googleapis.com/auth/youtube.upload"
    }
    response = requests.post(device_auth_url, data=payload)
    if response.status_code != 200:
        raise Exception(f"Ошибка получения кода устройства: {response.status_code} - {response.text}")

    device_data = response.json()

    # Передача ссылки и кода на фронтенд
    verification_url = device_data["verification_url"]
    user_code = device_data["user_code"]
    print(f"Ссылка для перехода: {verification_url}")
    print(f"Код для вставки: {user_code}")

    # Возвращаем на фронтенд ссылку и код
    return {
        "verification_url": verification_url,
        "user_code": user_code,
        "device_code": device_data["device_code"],
        "interval": device_data["interval"]
    }


def wait_for_authorization(client_id, client_secret, device_code, interval=5.0):
    token_url = "https://oauth2.googleapis.com/token"

    while True:
        time.sleep(interval)
        token_payload = {
            "client_id": client_id,
            "client_secret": client_secret,
            "device_code": device_code,
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code"
        }
        token_response = requests.post(token_url, data=token_payload)
        if token_response.status_code == 200:
            # Успешная авторизация
            return token_response.json()
        elif token_response.json().get("error") == "authorization_pending":
            print("Ожидание авторизации пользователя...")
        else:
            # Ошибка при авторизации
            raise Exception(f"Ошибка авторизации устройства: {token_response.status_code} - {token_response.text}")


def refresh_access_token(client_id, client_secret, refresh_token):
    """
    Обновление access_token с использованием refresh_token.
    """
    token_url = "https://oauth2.googleapis.com/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    response = requests.post(token_url, data=payload)
    if response.status_code == 200:
        token_data = response.json()
        print("Токен успешно обновлен.")
        return token_data["access_token"]
    else:
        raise Exception(f"Ошибка обновления токена: {response.status_code} - {response.text}")
