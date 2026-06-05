# Write a Python program to search for a word in a string using re.search().
import re

text = "Python is easy and powerful"

result = re.search("easy", text)

if result:
    print("Word found in string")
else:
    print("Word not found")



# Write a Python program to match a word in a string using re.match().
import re

text = "Python is easy and powerful"

result = re.match("Python", text)

if result:
    print("Word matches at the beginning")
else:
    print("No match at the beginning")





#-----------------------------------------------Practical Example-------------------------------------#

# Write a Python program to search for a word in a string using re.search(). 
import re

text = "Python is a powerful programming language"

result = re.search("powerful", text)

if result:
    print("Word found!")
else:
    print("Word not found!")





#Write a Python program to match a word in a string using re.match().
import re

text = "Python is a powerful programming language"

result = re.match("Python", text)

if result:
    print("Word matched at the beginning!")
else:
    print("No match at the beginning!")