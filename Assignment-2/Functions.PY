# Write a Python program to create a function that takes a string as input and prints it.
def show_str(text):
    print(text)
show_str("Hello Python")



# Write a Python program to create a calculator using functions.
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
n1 = 10
n2 = 5
print("Addition:", add(n1, n2))
print("Subtraction:", subtract(n1, n2))
print("Multiplication:", multiply(n1, n2))
print("Division:", divide(n1, n2))


#----------------------------------Practical Examples-------------------------------------#

# 19) Write a Python program to print a string using a function.
def print_string(text):
    print(text)
print_string("Hello, World!")


# 20) Write a Python program to create a parameterized function that takes two arguments and prints their sum.
def sum(a, b):
    print(a + b)
sum(10, 5)


# 21) Write a Python program to create a lambda function with one expression. 
square = lambda x: x * x
print(square(5))

# 22) Write a Python program to create a lambda function with two expressions.
add = lambda x, y: x + y
print(add(10, 5))
