from subprocess import call
from os import system
import time

# BETA SYSTEM, NEW UPDATED VERSION COMING SOON



def clear():
    system('clear')


def show_balance():
  print(f"Your Balance = ${balance:.2f}")


def deposit():
  amount = float(input("Enter amount to deposit: "))
  if amount < 0:
    print("Not a valid amount.")
    return 0
  else:
      return amount
  


def withdraw():
  amount = float(input("Enter amount to be withdrawn: "))
  if amount > balance:
    print("Not enough balance.")
  elif amount < 0:
    print("Amount must be positive.")
  else:
    return amount
      
balance = 0
          
print("=== Bank ===\n")
print("1. Show Balance")
print("2. Withdraw")
print("3. Deposit")
print("4. Exit")
print("============\n")
          
choice = input("\n> ")
          
if choice == "1":
  show_balance()
  time.sleep(2)
  call(["python", "CSS/menu.py"])
          
elif choice == "2":  
  if withdraw() is not None:
    balance -= withdraw()
    time.sleep(2)
    call(["python", "CSS/menu.py"])
          
elif choice == "3":
  balance += deposit()
  time.sleep(2)
  call(["python", "CSS/menu.py"])
              
elif choice == "4":
  call(["python", "CSS/menu.py"])
  
          
else:
  print("That is not a valid number.")
  time.sleep(2)
  call(["python", "CSS/menu.py"])
        