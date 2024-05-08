# Parent class - Base class
# Child class - derived class

# Creating a Parent class
class Person:
    def __init__(self, fname, lname): # Default constructor
        self.firstname = fname
        self.lastname = lname
    
    def printname(self): # Method
        print(f"My name is {self.firstname} {self.lastname}")

    def __str__(self):
        return f"""First Name: {self.firstname}\nLast Name: {self.lastname}"""
    
p1 = Person("John", "Doe") # create an object of the class
print(p1) # print the object
p1.printname() # call the method printname

# Creating a Child class

# When call init from the child class it will override the init from the parent(base) class
class Student(Person): # Inheritance from the Person class
    # pass # Use pass keyword when you do not want to add any other properties or methods
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) # fname and lname from base class
        self.graduationYear = year # year from the child class

    # def __init__(self, fname, lname): 
    #    super().__init__(fname, lname) # super() is used to call the parent(base) class constructor
    # same as Person.__init__(self, fname, lname)

    def __str__ (self):
        return f"\n\nFirst Name: {self.firstname}\nLast Name: {self.lastname}\nGraduation Year: {self.graduationYear}\n"    
    
    def welcome(self):
        print(f"Welcome {self.firstname}, {self.lastname} to the class of {self.graduationYear}")

s1 = Student("Anthony", "Olsen", 2027) # create an object of the class
print(s1)
s1.printname() # call the method printname from the base class

x = Student("Mike", "Olsen", 2025)
print(x)
x.printname()
x.welcome() # call the method welcome from the child class

s2 = Student("Anthony", "Su", 2025)
print(s2)
s2.printname()
s2.welcome()





