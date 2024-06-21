from subprocess import call

print("[===] Settings [===]")

print("\nYou're up to date.")
print("\n\n Version: 3.0.0")
print("--------------")
input2 = input("Press Q to go back to menu...\n\n")

if input2 == "q" or "Q":
  def open_pym_file():
      call(["python", "CSS/menu.py"])
  open_pym_file()


else:
  pass