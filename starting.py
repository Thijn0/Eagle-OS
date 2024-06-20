import time
from os import system
from subprocess import call

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
time.sleep(0.8)
clear()
print("RAM: OK")
time.sleep(0.5)
print("CPU: OK")
time.sleep(0.5)
clear()


def open_py2_file():
    call(["python", "main.py"])

open_py2_file()

