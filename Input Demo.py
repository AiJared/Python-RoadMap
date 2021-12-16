print('Create Account')
Username = input('Enter Username: ')
password = input('Enter password: ')
passwordb = input('Re-enter your password for confirmation: ')
if password == passwordb:
     print('Account created successfully.')
else:
    print('Password do not match')

print('Login now.')
Username2 = input('Enter username: ')
password2 = input('Enter password: ')
if Username == Username2 and password == password2:
    print('You have successfully logged in')
else:
    print('Incorrect Username or password')