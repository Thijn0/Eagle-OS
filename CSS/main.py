import time
from os import system
from subprocess import call
from colorama import Fore, Style

def clear():
    system('clear')

print("\n\n")
print(" ______          _____ _      ______ ")
print("|  ____|   /\   / ____| |    |  ____|")
print("| |__     /  \ | |  __| |    | |__   ")
print("|  __|   / /\ \| | |_ | |    |  __|  ")
print("| |____ / ____ \ |__| | |____| |____ ")
print("|______/_/    \_\_____|______|______|")


def show_loading_screen():
    print("=======================================")
    print(Fore.WHITE + "Welcome To Eagle OS | Terminal | 3.0.0")
    print("=======================================\n")
    width = 40
    total = 100
    interval = total / width
    for i in range(width + 1):
        progress = int(i * interval)
        bar = '█' * i
        stars = '-' * (width - i)
        loading_text = f"[{bar}{stars}] {progress}%"
        print(Fore.WHITE + loading_text, end='\r')
        time.sleep(0.1)
    print(Style.RESET_ALL)
    print("\n\n")

show_loading_screen()

# Laat login systeem runnen
# -------------------------

def open_py_file():
    call(["python", "Database/login.py"])

open_py_file()
# -------------------------


# -------------------------
#           MENU 
# -------------------------
print("\n===== MENU =====\n")

print(Fore.GREEN + "1. Settings       " + Fore.YELLOW + "2. Applications")
print(Fore.BLUE + "3. Mail           " + Fore.RED    + "4. Browser     ")
print(Fore.RED + "5. Bank           " + Fore.GREEN  + "6. About       ")

choice = input(Fore.WHITE + "\n> ")