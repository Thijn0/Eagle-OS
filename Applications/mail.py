from os import name
import time

print("Welcome to Eagle Mail")
time.sleep(1)
print("You have 3 mails")
print("which one do you want to open?")
choice = input("1, 2, 3 ")
if choice == "1":
  print("Mail by: EagleOSsystem")
  print("Welcome to Eagle OS, we are delighted to have you here")
  print("We hope you enjoy your stay with us")
elif choice == "2":
  print("Mail by: Eagl3Bank")
  print("Welcome to Eagle Bank,your acoount is hacked")
  print("reply and we will fix it")
elif choice == "3":
  print("Mail by: Your boss")
  print("Hello" + name + "you got a raise")
  print("can you come to the office")
  print("please reply")
  reply = input("Yes or no: ")
  if reply == "Yes":
    print ("I will see you soon")
  elif reply == "No":
    print("Ok, I will see you later")