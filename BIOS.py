import time


def clear ():
  system('clear')

clear()


print("=========================================")
time.sleep(0.01)
print("| BIOS      1.1.3                       |")
time.sleep(0.01)
print("| ------                                |")
time.sleep(0.01)
print("|   CPU Usage: 3.5%                     |")
time.sleep(0.01)
print("|   RAM: 2GB                            |")
time.sleep(0.01)
print("|                                       |")
time.sleep(0.01)
print("|                                       |")
time.sleep(0.01)
print("|                                       |")
time.sleep(0.01)
print("|  Enter to exit                        |")
time.sleep(0.01)
print("=========================================")
choice = input("Input:")
print("=========================================\n\n")
exec(open("main.py").read())
