from datetime import datetime
from colorama import Fore, Style

def backup_data():
    try:
        with open("data.txt", "r") as file:
            data = file.read()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"data_backup_{timestamp}.txt", "w") as backup_file:
            backup_file.write(data)
        return True
    except Exception as e:
        print(f"{Fore.RED}Error: Gagal membuat backup: {str(e)}{Style.RESET_ALL}")
        return False
