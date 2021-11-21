# Enables us to read a file that is not a py file using a python file
# Open a new file that is not python for example a text file then add in a content and save it in the same directory as your python file
# To read another file you have to import it to the python file
# Confirm if the file is readable
coun_file = open('C:/Users/Churchil Vogehere/Py_Roadmap/countries.txt', 'r')
print(coun_file.readable())
coun_file.close()

# Read the first line of our txt file
coun_file = open('C:/Users/Churchil Vogehere/Py_Roadmap/countries.txt', 'r')
print(coun_file.readline())
coun_file.close()

# Read all lines of the file in a list
coun_file = open('C:/Users/Churchil Vogehere/Py_Roadmap/countries.txt', 'r')
print(coun_file.readlines())
coun_file.close()

# Getting the lines separately
coun_file = open('C:/Users/Churchil Vogehere/Py_Roadmap/countries.txt', 'r')
print(coun_file.readlines()[0])
coun_file.close()

# Looping through the files using for loop
coun_file = open('C:/Users/Churchil Vogehere/Py_Roadmap/countries.txt', 'r')
for lines in coun_file.readlines():
    print(lines)
coun_file.close()