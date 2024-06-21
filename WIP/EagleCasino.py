from subprocess import call


print("Welcome to EagleCasino")
print("What do you want to do?")
casino_option = input("1. Play, 2. Buy Chips, 3. Exit ")


if casino_option == "1":
  pass

if casino_option == "2":
  pass

if casino_option == "3":
  call(["python", "CSS/menu.py"])