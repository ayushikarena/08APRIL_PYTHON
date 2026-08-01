#Write a Python program to apply the map() function to square a list of numbers
numbers = [1, 2, 3, 4, 5]

# Using map() to square each number
squared = list(map(lambda x: x**2, numbers))

print(squared)


print("------------------------------")

#Write a Python program that uses reduce() to find the product of a list of numbers.
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce() to find product
product = reduce(lambda x, y: x * y, numbers)

print(product)



print("------------------------------")

#Write a Python program that filters out even numbers using the filter() function.
numbers = [1, 2, 3, 4, 5, 6]

# Using filter() to keep only odd numbers
result = list(filter(lambda x: x % 2 != 0, numbers))

print(result)