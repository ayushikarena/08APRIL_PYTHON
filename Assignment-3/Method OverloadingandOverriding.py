# Write Python programs to demonstrate method overloading and method overriding.
class Calculator:
    def add(self, a, b=0, c=0):
        print(a + b + c)

obj = Calculator()

obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)


#-----------------------------------------------Practical Example-------------------------------------#
#Write a Python program to show method overloading. 
class Addition:
    def add(self, a, b=0, c=0):
        print("Sum =", a + b + c)

obj = Addition()

obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)



#  Write a Python program to show method overriding.
class Parent:
    def show(self):
        print("This is Parent Class")

class Child(Parent):
    def show(self):
        print("This is Child Class")

obj = Child()
obj.show()