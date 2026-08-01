# Write a Python program to handle exceptions in a simple calculator (division by zero, invalidinput).
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")


# Write a Python program to demonstrate handling multiple exceptions.
try:
    num = int(input("Enter a number: "))
    result = 100 / num

    file = open("data.txt", "r")
    print(file.read())

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter a number.")

except FileNotFoundError:
    print("Error: File not found.")

finally:
    print("Program execution completed.")



    


#-----------------------------------------------Practical Example-------------------------------------#
# Write a Python program to handle exceptions in a calculator. 
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")


# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).
try:
    file = open("data.txt", "r")

    a = 10
    b = 0
    print(a / b)

except FileNotFoundError:
    print("File not found.")

except ZeroDivisionError:
    print("Cannot divide by zero.")



# Write a Python program to handle file exceptions and use the finally block for closing the file. 
try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("File operation completed.")


# Write a Python program to print custom exceptions.
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))

    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")

    print("You entered:", num)

except NegativeNumberError as e:
    print("Custom Exception:", e)