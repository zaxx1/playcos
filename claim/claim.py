import requests
import json
import yaml
from colorama import Fore, Style

with open("config/headers.json", "r") as file:
    BASE_HEADERS = json.load(file)

with open("config/urls.yaml", "r") as file:
    urls = yaml.safe_load(file)
    CLAIM_URL = urls["claim_url"]

def claim(access_token):
    headers = BASE_HEADERS.copy()
    headers["authorization"] = f"Bearer {access_token}"
    try:
        response = requests.post(CLAIM_URL, headers=headers, json={})
        if response.status_code == 200:
            data = response.json()
            point = data.get("amount", 0)
            username = data.get("user", {}).get("firstName", "Tidak Diketahui")
            print(f"{Fore.GREEN}Klaim berhasil! Username: {username}, Poin: {point}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Klaim gagal, kode status: {response.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error klaim: {str(e)}{Style.RESET_ALL}")
