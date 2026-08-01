# Practical Example 1: How does the Python code structure work?

name = input("Enter your name: ")

if name == "":
    print("No name entered")
else:
    print("Hello", name)


print("----------------------------------")
#Practical Example 2: How to create variables in Python?

name = "Aayushi"   # string
age = 20           # integer
marks = 85.5       # float

print("Name:", name)
print("Age:", age)
print("Marks:", marks)


print("----------------------------------")
#Practical Example 3: How to take user input using the input() function.

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Name is:", name)
print("Age is:", age)



print("----------------------------------")
#Practical Example 4: How to check the type of a variable dynamically using type().

a = 10
b = 5.5
c = "Hello"

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))