# Enables writing on the external file, appending to it and creating a new file
# Writing a new file
coun_file = open('C:/Users/Churchil Vogehere/Py_Roadmap/countries.txt', 'w')
coun_file.write('This is the new text')

# Creating a new file
coun_file = open('C:/Users/Churchil Vogehere/Py_Roadmap/country.txt', 'w')
coun_file.write('This is the new country file')

# Apend something to our file
coun_file = open('C:/Users/Churchil Vogehere/Py_Roadmap/countries.txt', 'a')
coun_file.write('\nThis is a new line')

# Writing a python file on another python file
coun_file = open('C:/Users/Churchil Vogehere/Py_Roadmap/new.py', 'w')
coun_file.write('print(\'This is a new python file\')')