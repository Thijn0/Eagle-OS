from os import PRIO_PGRP


print("Welcome to EagleSport")
print("What do you want to watch?")
sportchoice = input("1. MLS, 2. NBA, 3. MLB, 4. Premier League, 5. Bundesliga ")
if sportchoice == "1":
  print("Loading MLS")
  print("You will be redirected to MLS")
  print("https://www.mlssoccer.com/schedule/tv-and-streaming#competition=all&club=all&date=2024-06-21")
elif sportchoice == "2":
  print("Loading NBA")
  print("You will be redirected to NBA")
  print("https://www.nba.com/watch/nba-tv")
elif sportchoice == "3":
  print("Loading MLB")
  print("You will be redirected to MLB")
  print("https://www.mlb.com/live-stream-games")
elif sportchoice == "4":
  print("Loading Premier League")
  print("You will be redirected to Premier League")
  print("https://www.premierleague.com/live")
elif sportchoice == "5":
  print("Loading Bundesliga")
  print("You will be redirected to Bundesliga")
  print("https://www.bundesliga.com/en/live")
else:
  print("Sorry, we don't have that sport.")