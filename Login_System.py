print("Create account")
username = input("Enter username: ")
password = input("Enter password: ")
passwordb = input("Re-enter the password for confirmation: ")
if password == passwordb:
    print("The account has been created successfully")
else:
    print("The passwords do not match!")

print("Login now!")
username2 = input("Enter the username: ")
password2 = input("Enter the password: ")

if username == username2 and password == password2:
    print("You have loged in successfully.")
else:
    print("Incorrect username or password. Please try again!")