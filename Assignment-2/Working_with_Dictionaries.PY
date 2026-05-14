# Write a Python program to update a value in a dictionary.
dict = {
    "name": "Aayushi",
    "age": 20,
    "city": "Rajkot",
    "course": "Python",
    "marks": 85,
    "grade": "A"
}
dict["age"] = 21
print(dict)

# Write a Python program to merge two lists into one dictionary using a loop
keys = ["name", "age", "city"]
values = ["Aayushi", 20, "Rajkot"]
dict = {}
for i in range(len(keys)):
    dict[keys[i]] = values[i]
print(dict)

#----------------------------------Practical Examples-------------------------------------#

# 15) Write a Python program to update a value at a particular key in a dictionary.
dict = {
    "name": "Aayushi",
    "age": 20,
    "city": "Rajkot"
}
dict["age"] = 21
print(dict)


#  16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods.
dict = {
    "name": "Aayushi",
    "age": 20,
    "city": "Rajkot"
}
print("Keys:", dict.keys())
print("Values:", dict.values())


# 17) Write a Python program to convert two lists into one dictionary using a for loop.
keys = ["name", "age", "city"]
values = ["Aayushi", 20, "Rajkot"]
dict = {}
for i in range(len(keys)):
    dict[keys[i]] = values[i]
print(dict)


# 18) Write a Python program to count how many times each character appears in a string.
string = "hello"
Count = {}
for char in string:
    if char in Count:
        Count[char] += 1
    else:
        Count[char] = 1
print(Count)