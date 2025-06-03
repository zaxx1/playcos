from datetime import datetime
from core.utils import print_colored, Fore

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print_colored(f"[{timestamp}] {message}", Fore.BLUE)