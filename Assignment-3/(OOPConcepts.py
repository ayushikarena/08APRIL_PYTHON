# Write a Python program to create a class and access its properties using an object.
class Student:
    name = "Amit"
    age = 20

s1 = Student()

print("Name:", s1.name)
print("Age:", s1.age)






#-----------------------------------------------Practical Example-------------------------------------#
# Write a Python program to create a class and access the properties of the class using an object. 
class Student:
    name = "Amit"
    age = 20
s1 = Student()
print("Name:", s1.name)
print("Age:", s1.age)


#Write a Python program to demonstrate the use of local and global variables in a class.
x = 100

class Demo:
    def show(self):
        
        y = 50

        print("Global Variable:", x)
        print("Local Variable:", y)

obj = Demo()
obj.show()