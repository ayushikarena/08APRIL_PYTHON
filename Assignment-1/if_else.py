#Practical Example 5: Write a Python program to find greater and less than a number using if_else.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
else:
    print("Second number is greater")


print("----------------------------------")
#Practical Example 6: Write a Python program to check if a number is prime using if_else.
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


print("----------------------------------")
#Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder
per = float(input("Enter percentage: "))

if per >= 90:
    print("Grade A")
elif per >= 75:
    print("Grade B")
elif per >= 50:
    print("Grade C")
else:
    print("Fail")


print("----------------------------------")
#Practical Example 8: Write a Python program to check if a person is eligible to donate bloodusing a nested if.
age = int(input("Enter age: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if weight >= 50:
        print("Eligible to donate blood")
    else:
        print("Not eligible (Weight should be at least 50 kg)")
else:
    print("Not eligible (Age should be at least 18)")




