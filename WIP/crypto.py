from moneysystem import balance
from colorama import Fore, Style

print("Welcome to this crypto platform.")
user_name = input("Username: ")
password = input("Password: ")
print("Hi " + user_name)
print("NOTE: Crytpo is outdated in version 2.2")
print("Wich activity would you like to do? ")

activity = input("\n>Watch Course\n>Buy Crypto\n\n>")
if activity == "Watch Course":
  print("\nBitcoin:")
  print(Fore.GREEN + "Bitcoin: +0,37%"	)

  print("\nDogecoin:")
  print(Fore.GREEN + "Dogecoin: +0,10%")
  

  print("\nEthereum:")
  print(Fore.RED + "Ethereum: -0,58%")
  


elif activity == "Buy Crypto":
  print("Which crypto coin do you want to buy?")
  crypto = input("\n>Bitcoin\n>Dogecoin\n>Ethereum\n\n>")
  if crypto == "Bitcoin":
    number = input("How many Bitcoins do you want to buy? ")
    print("Buying " + number + " Bitcoins")
    print("......")
    time.sleep(1)
    print("**....")
    time.sleep(1)
    print("****..")
    time.sleep(1)
    print("******")
    print("You succesfully bought " + number + " Bitcoins.")
    print("your balance is", balance)
    

  elif crypto == "Dogecoin":
    number = input("How many Dogecoins do you want to buy? ")
    print("Buying " + number + " Dogecoins")
    print("......")
    time.sleep(1)
    print("**....")
    time.sleep(1)
    print("****..")
    time.sleep(1)
    print("******")
    print("You succesfully bought " + number + " Dogecoins.")
    print("your balance is", balance)

  elif crypto == "Ethereum":
    number = input("How many Ethereums do you want to buy? ")
    print("Buying " + number + " Ethereums")
    print("......")
    time.sleep(1)
    print("**....")
    time.sleep(1)
    print("****..")
    time.sleep(1)
    print("******")
    print("You succesfully bought " + number + " Ethereums.")
    print("your balance is", balance)

  else:
    print("Sorry we don't have that crypto.")
    exit()