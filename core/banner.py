from core.utils import print_colored, Fore, Style

def print_banner():
    BANNER = f"""
{Fore.CYAN}╔══════════════════════════════════════════════╗
║       🌟 CrossPlay Bot - Automated Claim     ║
║   Automate your CrossPlay account tasks!     ║
║  Developed by: https://t.me/sentineldiscus   ║
╚══════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print_colored(BANNER, Fore.CYAN)
