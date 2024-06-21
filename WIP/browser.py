import time
from os import system

print ("welcome to the EagleOS Browser")
time.sleep (1)
print("what do you want to search?")
search = input("search: ")
print("good choice")
print ("searching...")
time.sleep (1)
print("Loading...")
if search == "Youtube" or "youtube":
  print("https://www.youtube.com/")
elif search == "Google" or "google":
  print("https://www.google.com/")
elif search == "Spotify":
  print("https://open.spotify.com/")
elif search == "Discord":
  print("https://discord.com/channels/@me")
elif search == "BBC":
  print("https://www.bbc.com/")
else:
  print("sorry, we couldn't find that")