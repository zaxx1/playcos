from colorama import Fore, Style

def read_encoded_messages():
    try:
        with open("data.txt", "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File data.txt tidak ditemukan!{Style.RESET_ALL}")
        return []
    except Exception as e:
        print(f"{Fore.RED}Error: Gagal membaca data.txt: {str(e)}{Style.RESET_ALL}")
        return []
