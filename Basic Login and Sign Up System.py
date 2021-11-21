print('Create an account now.')
username = input('Enter your username: ')
password = input('Enter your password: ')

print('Your account has been created successfully.')
print('Login now!')

username2 = input('Enter your username: ')
password2 = input('Enter your password: ')

if username == username2 and password == password2:
    print('Logged in successfully.')
else:
    print('Invalid credentials.')