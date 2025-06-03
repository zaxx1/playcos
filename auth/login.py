import requests
import json
import yaml
from colorama import Fore, Style

with open("config/headers.json", "r") as file:
    BASE_HEADERS = json.load(file)

with open("config/urls.yaml", "r") as file:
    urls = yaml.safe_load(file)
    LOGIN_URL = urls["login_url"]

def login(encoded_message):
    payload = {"encodedMessage": encoded_message}
    headers = BASE_HEADERS.copy()
    try:
        response = requests.post(LOGIN_URL, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            access_token = data.get("accessToken")
            if access_token:
                print(f"{Fore.GREEN}ログイン成功！{Style.RESET_ALL}")
                return access_token
            else:
                print(f"{Fore.RED}アクセストークンの取得に失敗しました{Style.RESET_ALL}")
                return None
        else:
            print(f"{Fore.RED}ログイン失敗、ステータスコード: {response.status_code}{Style.RESET_ALL}")
            return None
    except Exception as e:
        print(f"{Fore.RED}ログインエラー: {str(e)}{Style.RESET_ALL}")
        return None