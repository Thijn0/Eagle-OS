from moneysystem import balance

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
      paymethod = input("1. EagleBank")
      if paymethod == "1":
        pay = input("Click P to pay: ")
        if pay == "P":
          pass

        else:
          print("Payment not succeeded.")
          pass


    if proceed == "No":
      print("Order canceled")
  
  if buyoption == "2":
   print("Loading receipt")
   receipt2 = ("$2,300")
  print("Do you want to proceed the order?")
  proceed = input("Yes or No ")
  if proceed == "Yes":
    print("Your order has been placed")
    print("Please select your paymethod")
    paymethod = input("1. EagleBank")
    if paymethod == "1":
      pay = input("Click P to pay: ")
      if pay == "P":
        pass
      if proceed == "No":
        print("Order canceled")
  
  if buyoption == "3":
    print("Loading receipt")
    receipt3 = ("$430")
    print("Do you want to proceed the order?")
    proceed = input("Yes or No ")
    if proceed == "Yes":
      print("Your order has been placed")
      print("Please select your paymethod")
      paymethod = input("1. EagleBank")
      if paymethod == "1":
        pay = input("Click P to pay: ")
        if pay == "P":
          pass
      if proceed == "No":
        print("Order canceled")
      else:
        print("Payment not succeeded.")
