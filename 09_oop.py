# =====================================================
# TOPIC 9: OBJECT ORIENTED PROGRAMMING (OOP)
# Classes, Objects, Constructor, Inheritance, Encapsulation, Polymorphism
# =====================================================

# ---------- 1. CLASS AND OBJECT ----------
# A class is a blueprint. An object is an instance created from that blueprint.

class Student:
    pass   # empty class for now

s1 = Student()    # creating an object (instance) of the class
print(type(s1))


# ---------- 2. CONSTRUCTOR (__init__ method) ----------
# __init__ runs automatically when an object is created. Used to set initial values.

class Student:
    def __init__(self, name, age):
        self.name = name      # self.name -> instance variable (belongs to the object)
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Aman", 21)
s2 = Student("Riya", 20)

s1.display()    # Name: Aman, Age: 21
s2.display()    # Name: Riya, Age: 20


# ---------- 3. INSTANCE VARIABLES vs CLASS VARIABLES ----------
class Student:
    school_name = "ABC School"     # class variable -> SAME for all objects

    def __init__(self, name):
        self.name = name           # instance variable -> DIFFERENT for each object

s1 = Student("Aman")
s2 = Student("Riya")

print(s1.name, s1.school_name)    # Aman ABC School
print(s2.name, s2.school_name)    # Riya ABC School


# ---------- 4. METHODS ----------
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()
print(calc.add(10, 5))         # 15
print(calc.subtract(10, 5))    # 5


# ---------- 5. INHERITANCE ----------
# A class can inherit properties and methods from another class.

class Animal:                      # Parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):                 # Child class inherits from Animal
    def speak(self):               # method overriding - redefining parent method
        print(f"{self.name} barks.")

class Cat(Animal):
    pass    # Cat will use the parent's speak() method as it is

d = Dog("Tommy")
c = Cat("Kitty")

d.speak()    # Tommy barks.
c.speak()    # Kitty makes a sound.


# ---------- 6. super() FUNCTION ----------
# Used to call the parent class's constructor/method from the child class

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    # calls the parent class's __init__
        self.breed = breed

    def display(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

d = Dog("Tommy", "Labrador")
d.display()


# ---------- 7. ENCAPSULATION (Private Variables) ----------
# Restricting direct access to some variables using underscore convention

class Account:
    def __init__(self, balance):
        self.__balance = balance     # double underscore = private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())    # 1500
# print(acc.__balance)      # ERROR - cannot access private variable directly


# ---------- 8. POLYMORPHISM ----------
# Same method name behaves differently for different classes

class Bird:
    def sound(self):
        print("Birds make different sounds")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

class Crow(Bird):
    def sound(self):
        print("Crow caws")

for bird in (Sparrow(), Crow()):
    bird.sound()    # same method name, different behavior


# ---------- 9. MAGIC / DUNDER METHODS ----------
# Special methods that start and end with double underscores

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):              # called automatically when we print the object
        return f"Book: {self.title}"

b = Book("Python Basics")
print(b)    # Book: Python Basics (instead of a memory address)
