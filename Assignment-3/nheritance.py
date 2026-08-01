# Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).
class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):
    pass

obj = Child()
obj.show()



#-----------------------------------------------Practical Example-------------------------------------#
# Write a Python program to show single inheritance. 
class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):
    pass

obj = Child()
obj.show()


# Write aPython program to show multilevel inheritance. 
class Grandparent:
    def show1(self):
        print("Grandparent Class")

class Parent(Grandparent):
    pass

class Child(Parent):
    pass

obj = Child()
obj.show1()



# Write a Python program to show multipleinheritance. 
class Father:
    def show1(self):
        print("Father Class")

class Mother:
    def show2(self):
        print("Mother Class")

class Child(Father, Mother):
    pass

obj = Child()
obj.show1()
obj.show2()



# Write a Python program to show hierarchical inheritance. 
class Parent:
    def show(self):
        print("Parent Class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.show()
obj2.show()



# Write a Pythonprogram to show hybrid inheritance. 
class A:
    def show1(self):
        print("Class A")

class B(A):
    def show2(self):
        print("Class B")

class C(A):
    def show3(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.show1()
obj.show2()
obj.show3()



# Write a Python program to demonstrate the use ofsuper() in inheritance
class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

obj = Child()