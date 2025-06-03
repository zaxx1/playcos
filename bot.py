import time
import random
import yaml
from auth.login import login
from claim.claim import claim
from core.file_reader import read_encoded_messages
from core.banner import print_banner
from data.data_backup import backup_data
from colorama import init, Fore, Style

# Inisialisasi colorama untuk warna terminal
init(autoreset=True)

# Membaca konfigurasi dari file YAML
with open("config/settings.yaml", "r") as file:
    config = yaml.safe_load(file)
    WAIT_TIME_MIN = config["wait_time_min"]  # Waktu tunggu minimal (detik)
    WAIT_TIME_MAX = config["wait_time_max"]  # Waktu tunggu maksimal (detik)
    SLEEP_BETWEEN_ACCOUNTS = config["sleep_between_accounts"]  # Jeda antar akun

def main():
    print_banner()  # Menampilkan banner
    backup_data()  # Membuat backup data
    
    # Membaca pesan terenkripsi dari file
    encoded_messages = read_encoded_messages()
    if not encoded_messages:
        print(f"{Fore.RED}Akun tidak ditemukan. Mohon masukkan encodedMessage di data.txt{Style.RESET_ALL}")
        return
    
    # Looping utama
    while True:
        for encoded_message in encoded_messages:
            # Proses login
            access_token = login(encoded_message)
            
            if access_token:
                claim(access_token)  # Klaim poin jika login berhasil
            else:
                print(f"{Fore.RED}Melewati klaim karena login gagal{Style.RESET_ALL}")
            
            # Jeda sebelum akun berikutnya
            print(f"{Fore.YELLOW}Menunggu {SLEEP_BETWEEN_ACCOUNTS} detik untuk akun berikutnya...{Style.RESET_ALL}")
            time.sleep(SLEEP_BETWEEN_ACCOUNTS)
        
        # Waktu tunggu acak sebelum loop berikutnya
        wait_time = random.randint(WAIT_TIME_MIN, WAIT_TIME_MAX)
        minutes = wait_time // 60
        seconds = wait_time % 60
        print(f"{Fore.YELLOW}Akan memulai loop berikutnya dalam {minutes} menit {seconds} detik...{Style.RESET_ALL}")
        time.sleep(wait_time)

if __name__ == "__main__":
    main()
