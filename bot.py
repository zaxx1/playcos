import time
import random
import yaml
from auth.login import login
from claim.claim import claim
from core.file_reader import read_encoded_messages
from core.banner import print_banner
from data.data_backup import backup_data
from colorama import init, Fore, Style

init(autoreset=True)

with open("config/settings.yaml", "r") as file:
    config = yaml.safe_load(file)
    WAIT_TIME_MIN = config["wait_time_min"]
    WAIT_TIME_MAX = config["wait_time_max"]
    SLEEP_BETWEEN_ACCOUNTS = config["sleep_between_accounts"]
    PROXY_ENABLED = config.get("proxy", {}).get("enabled", False)
    PROXIES = {
        "http": config.get("proxy", {}).get("http"),
        "https": config.get("proxy", {}).get("https"),
    } if PROXY_ENABLED else None

def main():
    print_banner()
    backup_data()
    
    encoded_messages = read_encoded_messages()
    if not encoded_messages:
        print(f"{Fore.RED}Akun tidak ditemukan. Mohon masukkan encodedMessage di data.txt{Style.RESET_ALL}")
        return
    
    # Looping utama
    while True:
        for encoded_message in encoded_messages:
            # Proses login
            access_token = login(encoded_message, proxies=PROXIES)
            
            if access_token:
                claim(access_token, proxies=PROXIES)
            else:
                print(f"{Fore.RED}Melewati klaim karena login gagal{Style.RESET_ALL}")
            
            print(f"{Fore.YELLOW}Menunggu {SLEEP_BETWEEN_ACCOUNTS} detik untuk akun berikutnya...{Style.RESET_ALL}")
            time.sleep(SLEEP_BETWEEN_ACCOUNTS)
        
        wait_time = random.randint(WAIT_TIME_MIN, WAIT_TIME_MAX)
        minutes = wait_time // 60
        seconds = wait_time % 60
        print(f"{Fore.YELLOW}Akan memulai loop berikutnya dalam {minutes} menit {seconds} detik...{Style.RESET_ALL}")
        time.sleep(wait_time)

if __name__ == "__main__":
    main()
