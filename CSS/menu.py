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
    print("Test2")

elif choice == "3":
    print("Test3")

elif choice == "4":
    print("Test4")

elif choice == "5":
    print("Test5")

elif choice == "6":
    print("Test6")

else:
    print("Not valid.")