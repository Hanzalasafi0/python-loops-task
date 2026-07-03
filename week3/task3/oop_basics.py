# Week 3 - Task 3
# Introduction to Object-Oriented Programming (OOP)

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Child Class (Inheritance)
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    # Polymorphism (Method Overriding)
    def display(self):
        print("Student Information")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Object Creation
student1 = Student("Hanzala Safi", 20, "Python Development")

# Calling Method
student1.display()
