import time
from os import system
from subprocess import call

def clear():
    system('clear')

print(" ______          _____ _      ______ ")
print("|  ____|   /\   / ____| |    |  ____|")
print("| |__     /  \ | |  __| |    | |__   ")
print("|  __|   / /\ \| | |_ | |    |  __|  ")
print("| |____ / ____ \ |__| | |____| |____ ")
print("|______/_/    \_\_____|______|______|")

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
    call(["python", "CSS/main.py"])

open_py2_file()

