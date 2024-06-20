import time
from os import system
from subprocess import call
from colorama import Fore, Style

def clear():
    system('clear')

print("\n\n")
print(" ______ _______  _____   _        _____  ")
print("|  ___| | |_| | |  ___| | |      |  ___| ")
print("| |___  |  _  | | |     | |      | |___  ")
print("|  ___| | | | | | |     | |      |  ___| ")
print("| |___  | | | | | |__|| | |____  | |___  ")
print("|_____| |_| |_| |_____| |______| |_____| ")


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

print("\n===== MENU =====\n")


