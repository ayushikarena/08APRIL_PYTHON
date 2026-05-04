# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continuestatement. List1 = ['apple', 'banana', 'mango']
List1 = ['apple', 'banana', 'mango']

for item in List1:
    if item == 'banana':
        continue
    print(item)



print("------------------------------")



#Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement.
List1 = ['apple', 'banana', 'mango']

for item in List1:
    if item == 'banana':
        break
    print(item)