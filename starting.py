import time
from os import system
from subprocess import call
from colorama import Fore, Style

def clear():
    system('clear')

print(" ______ _______  _____   _        _____  ")
print("|  ___| | |_| | |  ___| | |      |  ___| ")
print("| |___  |  _  | | |     | |      | |___  ")
print("|  ___| | | | | | |     | |      |  ___| ")
print("| |___  | | | | | |__|| | |____  | |___  ")
print("|_____| |_| |_| |_____| |______| |_____| ")

print("\n\n")
time.sleep(2)

print("Checking System...")
time.sleep(1)
print("RAM: OK")
time.sleep(0.5)
print("CPU: OK")
time.sleep(0.5)
clear()

print("Enter BIOS?")
print("1: Yes")
print("2: No\n")

bios = input("")

if bios == "1":
    exec(open("BIOS.py").read())

else:
    exec(open("main.py").read())

clear()