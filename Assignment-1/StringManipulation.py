# Write a Python program to demonstrate string slicing.
text = "Python Programming"
print("Original String:", text)

print("From index 2 to 6:", text[2:6])       
print("From start to index 5:", text[:5])     
print("From index 7 to end:", text[7:])       
print("Every alternate character:", text[::2])
print("Reversed string:", text[::-1])        

print("------------------------------")

#Write a Python program that manipulates and prints strings using various string methods.
text = "  hello python world  "

print("Original String:", text)

# Case conversion
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalized:", text.capitalize())

# Whitespace removal
print("Strip:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())

# Replacement
print("Replace 'python' with 'programming':", text.replace("python", "programming"))

# Splitting and joining
words = text.strip().split()
print("Split into words:", words)
print("Joined with '-':", "-".join(words))

# Searching
print("Index of 'python':", text.find("python"))

# Checking methods
print("Is alphabetic:", text.isalpha())
print("Is lowercase:", text.islower())