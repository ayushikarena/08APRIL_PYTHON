# Write a Python program to iterate over a list using a for loop.
list = [10, 20, 30, 40, 50]
for e in list:
    print(e)

# Write a Python program to sort a list using both sort() and sorted().
list = [40, 10, 30, 20]
list.sort()
print("Using sort():", list)
newlist = sorted(list)
print("Using sorted():", newlist)

#---------------------------------Practical Examples-------------------------------------#

# 5) Write a Python program to iterate through a list and print each element. 

list = [10, 20, 30, 40]
for item in list:
    print(item)

#  6) Write a Python program to insert elements into an empty list using a for loop and append()
list = []
for i in range(1, 6):
   list.append(i)
print(list)

