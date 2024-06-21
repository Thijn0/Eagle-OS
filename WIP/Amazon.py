print("Welcome to Amazon")
print("What do you like to do")
amazon = input("1. Buy, 2. Sell, 3. Return 4. Exit ")
if amazon == "1":
  print("What do you want to buy?")
  buyoption = input("1. Gaming PC, 2. HD Television, 3. Playstation 5")
  if buyoption == "1":
    print("Loading receipt")
    receipt = ("$953,95")
    print("Whould you like to proceed the order?")
    proceed = input("Yes or No ")
    if proceed == "Yes":
      print("Your order has been placed")
      print("Please select your paymethod")
      paymethod = input("1. Card (VI, 3. Paypal")