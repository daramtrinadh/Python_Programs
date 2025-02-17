#Basic Inheritance
class Vehicle():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        return f"{self.make} with {self.model} in year {self.year}"


class Car(Vehicle):
    def __init__(self,make,model,year,no_of_doors):
        super().__init__(make,model,year)
        self.no_of_doors=no_of_doors
    def display(self):
        return f"The {self.model} car is manufactured in {self.year} with {self.no_of_doors} doors by {self.make}"



vehicle=Vehicle("Make","Buggati",2003)
car=Car("Make","Buggati",2003,4)
print(vehicle.display())
print(car.display())




##Method Overriding

# Define a class Animal with a method speak().
# Create two subclasses, Dog and Cat, that override the speak() method to return "Woof!" and "Meow!" respectively.
# Demonstrate polymorphism by creating a list of animals and calling their speak() method.

# class Animal():
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return f"{self.name} is speaking"
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} is Wooffing"
#
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} is Meowing"
#
# animals = [Animal("Generic Animal"), Dog("Buddy"), Cat("Whiskers")]
#
# for animal in animals:
#     print(animal.speak())

#Multiple Inheritance
# Create two classes, Flyable (with a method fly()) and Swimmable (with a method swim()).
# Then, create a class Duck that inherits from both classes.
# Implement the methods in the Duck class to print appropriate messages.

# class Flyable():
#     def __init__(self,name):
#         self.name=name
#     def fly(self):
#         return f"{self.name} flying"
#
# class Swimmable():
#     def __init__(self,name):
#         self.name=name
#     def swim(self):
#         return f"{self.name} is Swimming"
# class Duck(Flyable,Swimmable):
#     def __init__(self,name):
#         super().__init__(name)
#
#     def quack(self):
#         return f"{self.name} is quacking"
# duck=Duck("messi")
# print(duck.swim())
# print(duck.fly())

# Using super():
# Create a base class called Person with an initializer that takes name and age.
# Create a subclass called Student that adds an attribute for student_id.
# Use the super() function to call the parent class's initializer.

# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def introduce(self):
#
#
# class Student(Person):
#     def __init(self,name,age,student_id):
#         self.student_id=student_id
#         super().__init__(name,age)


class Branch():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class SubBranch(Branch):
    def call(self):
        return self.age

# B=Branch("Trinadh",21)
S=SubBranch("Trinadh",21)
print(S.call())