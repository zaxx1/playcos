from colorama import init, Fore, Style

init(autoreset=True)

def print_colored(message, color=Fore.WHITE):
    print(f"{color}{message}{Style.RESET_ALL}")