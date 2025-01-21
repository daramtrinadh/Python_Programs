# Create a Class and Object
#
# Create a class Person with attributes name and age.
# Create an object of this class and print its attributes.


class Person():
    species="Home Sepians" #class Variable

    def __init__(self,name,age): #class constructors using __init__
        self.name=name
        self.age=age

    def introduce(self): #class method
        return f"My name is {self.name} and i am {self.age} years old."

#Inheritance

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id

    def study(self):
        return f"Student with {self.student_id} named {self.name} is studying with age {self.age}"


person1=Person("Trinadh",21)
student=Student("Trinadh",21,200303124188)
print(student.study())
