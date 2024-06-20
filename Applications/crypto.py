import balance
print("Welcome to this crypto platform.")
user_name = input("Username: ")
password = input("Password: ")
print("Hi " + user_name)
print("Wich activity would you like to do? ")
print("NOTE: This edition of the system is outdated and in V.2.2")
activity = input("\n>Watch Course\n>Buy Crypto\n\n>")
if activity == "Watch Chart":
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
    print("Your Balance" + balance)
    

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

  else:
    print("Sorry we don't have that crypto.")
    exit()