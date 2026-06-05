# Write a Python program to read the contents of a file and print them on the console.
file = open("myfile.txt", "r")
data = file.read()
print(data)
file.close()


# Write a Python program to write multiple strings into a file.
file = open("data.txt", "w")
file.write("Python\n")
file.write("Java\n")
file.write("C++\n")
file.close()

print("Data written successfully.")




#-----------------------------------------------Practical Example-------------------------------------#

#Write a Python program to create a file and print the string into the file. 
file = open("test.txt", "w")
file.write("Welcome to Python")
file.close()

print("String written into file.")


# Write a Python program to read a file and print the data on the console. 
file = open("test.txt", "r")
print(file.read())
file.close()


# Write a Python program to check the current position of the file cursor using tell().
file = open("test.txt", "r")
print("Current Position:", file.tell())
file.read(7)
print("New Position:", file.tell())
file.close()