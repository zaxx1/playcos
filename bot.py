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

def main():
    print_banner()
    backup_data()
    encoded_messages = read_encoded_messages()
    if not encoded_messages:
        print(f"{Fore.RED}アカウントが見つかりません。data.txtにencodedMessageを入力してください。{Style.RESET_ALL}")
        return
    while True:
        for encoded_message in encoded_messages:
            access_token = login(encoded_message)
            if access_token:
                claim(access_token)
            else:
                print(f"{Fore.RED}ログイン失敗のため、クレームをスキップします。{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}次のアカウントまで{SLEEP_BETWEEN_ACCOUNTS}秒待機...{Style.RESET_ALL}")
            time.sleep(SLEEP_BETWEEN_ACCOUNTS)
        wait_time = random.randint(WAIT_TIME_MIN, WAIT_TIME_MAX)
        print(f"{Fore.YELLOW}{wait_time // 60}分{wait_time % 60}秒後に次のループを開始...{Style.RESET_ALL}")
        time.sleep(wait_time)

if __name__ == "__main__":
    main()
