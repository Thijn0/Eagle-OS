def register():
    db = open("Database/data.txt", "r")
    username = input("Create Username: ")
    password = input("Create Password: ")
    password1 = input("Confirm Password: ")
    d = []
    f = []
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
  
    if password != password1:
        print("Passwords don't match, restart.")
        register()
    else:
      if len(password)<=6:
        print("Password too short, restart.")
        register()
     # elif username in db:
     #   print("Username exists, restart.")
     #   register()
      else:
          db = open("Database/data.txt", "a")
          db.write(username+", "+password+"\n")
          print("User created.")


def access():
    db = open("Database/data.txt", "r")
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")

    if not len(username or password)<1:
      d = []
      f = []
      for i in db:
          a,b = i.split(", ")
          b = b.strip()
          d.append(a)
          f.append(b)
      data = dict(zip(d, f))

      try:
         if data [username]:
            try:
                if password == data[username]:
                    print("Login Succesfull.")
                    print("Welcome back," , username)
                else:
                    print("Username or Password incorrect.")
                    home()

            except:
                print("Incorrect password or username.")
                home()
         else:
              print("Username doesn't exist.")
              home()
      except:
          print("Login Error.")
          home()
    else:
      print("Please enter a value.")
      home()

def home(option=None):
    option = input("Login | Register: ")
    if option == "Login":
        access()
    elif option == "Register":
        register()
    else:
        print("Please enter an option.")
home()
