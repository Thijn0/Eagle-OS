import time
from os import system
from subprocess import call
from colorama import Fore, Style

def clear():
    system('clear')

clear()


print("\n===== MENU =====\n")

print(Fore.GREEN + "1. Settings       " + Fore.YELLOW + "2. Applications")
print(Fore.BLUE + "3. Mail           " + Fore.RED    + "4. Browser     ")
print(Fore.RED + "5. Bank           " + Fore.GREEN  + "6. About       ")

choice = input(Fore.WHITE + "\n> ")

if choice == "1":
    def open_pys_file():
        call(["python", "Applications/settings.py"])
    open_pys_file()

elif choice == "2":
    def open_pya_file():
        call(["python", "CSS/apps.py"])
    open_pya_file()

elif choice == "3":
    def open_pym_file():
        call(["python", "Applications/mail.py"])
    open_pym_file()

elif choice == "4":
    def open_pyb_file():
        call(["python", "Applications/browser.py"])
    open_pyb_file()

elif choice == "5":
    def open_pybb_file():
        call(["python", "Applications/moneysystem.py"])
    open_pybb_file()

elif choice == "6":
    def open_pyab_file():
        call(["python", "Applications/about.py"])
    open_pyab_file()

else:
    print("Not valid.")