#imports
from colorama import Fore

#functions

def menu():
    print(f"---------------------------------")
    print(f"{Fore.BLUE}TO-DOs{Fore.RESET} management system")
    print(f"[{Fore.YELLOW}1{Fore.RESET}] View to-do")
    print(f"[{Fore.RED}2{Fore.RESET}] Edit to-do")
    print(f"[{Fore.BLUE}3{Fore.RESET}] Delete to-do")
    print(f"[{Fore.YELLOW}a{Fore.RESET}] Add to-do")
    print(f"[{Fore.RED}c{Fore.RESET}] Complete to-do")
    print(f"---------------------------------")
    int(input("Please select an option!: "))

menu()