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
          
coice = input("\n> ")
          
if choice == "1":
  show_balance()
          
elif choice == "2":
  balance -= withdraw()
          
elif choice == "3":
  balance += deposit()
              
elif choice == "4":
  pass
          
else:
  print("That is not a valid number.")
        