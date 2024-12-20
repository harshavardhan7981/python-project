user ={}
def Display_menu():
    print("\n---Login System---")
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    print("4. Exit")
    return input("Choose an option (1-4):")
def register_user():
    username = input("enter a username:")
    if username in user:
        print("username already exists! Please choose a different username.")
    else:
        password = input("enter a password:")
        user[username] = password
        print(f"User '{username}' registered successfully!")
def login_user():
    username = input("enter your username:")
    if username in user:
        password = input("enter your password:")
        if user[username] ==password:
            print(f"welcome,{username}! you are successfully logged in.")
        else:
            print("Incorrect password! Please try again.")
    else:
        print("User not found! Please register first ")
def change_password():
    username = input("Enter your name:")
    if username in user:
        old_password = input("Enter your current password:")
        if user[username]==old_password:
              new_password = input("Enter your new password:")
              user[username] = new_password
              print('password changed successfully!')
        else:
            print("current password is incorrect! please try again.")
    else:
        print("username not found! please try again.")
while True:
    choice = Display_menu()
    if choice == "1":
        register_user()
    elif choice =="2":
        login_user()
    elif choice =="3":
        change_password()
    elif choice =="4":
        print('exiting the login system.Goodbye!')
        break
    else:
         print("invalid choice! please choose a valid option.")