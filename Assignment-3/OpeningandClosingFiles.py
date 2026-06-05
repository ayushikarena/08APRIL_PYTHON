# Write a Python program to open a file in write mode, write some text, and then close it.
file = open("sample.txt", "w")
file.write("Welcome to Python Programming")
file.close()

print("Data written successfully.")






#-----------------------------------------------Practical Example-------------------------------------#

# Write a Python program to create a file and write a string into it
file = open("myfile.txt", "w")

file.write("Hello, World!")

file.close()

print("File created and string written successfully.")