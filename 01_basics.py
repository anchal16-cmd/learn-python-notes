# =====================================================
# TOPIC 1: PYTHON BASICS
# Variables, Data Types, Type Casting, Input/Output
# =====================================================

# ---------- 1. PRINT STATEMENT ----------
# print() is used to display output on the screen

print("Hello, Python!")

# You can print multiple things separated by commas
print("Hello", "World", 2026)

# sep changes the separator between values, end changes what comes after
print("Python", "Notes", sep=" - ", end="!\n")


# ---------- 2. VARIABLES ----------
# A variable is a name that stores a value.
# Python does NOT need you to declare the type (it auto-detects it).

name = "Rahul"        # string variable
age = 20               # integer variable
height = 5.9           # float variable
is_student = True      # boolean variable

print(name, age, height, is_student)

# Multiple variables in one line
x, y, z = 1, 2, 3
print(x, y, z)

# Same value to multiple variables
a = b = c = 100
print(a, b, c)


# ---------- 3. DATA TYPES IN PYTHON ----------
# int      -> whole numbers           e.g. 10, -5
# float    -> decimal numbers         e.g. 3.14
# str      -> text (string)           e.g. "hello"
# bool     -> True / False
# list     -> ordered, changeable     e.g. [1,2,3]
# tuple    -> ordered, unchangeable   e.g. (1,2,3)
# dict     -> key-value pairs         e.g. {"a":1}
# set      -> unordered, no duplicates e.g. {1,2,3}

num = 10
flo = 3.14
text = "Python"
flag = False

# type() function tells us the data type of a variable
print(type(num))    # <class 'int'>
print(type(flo))    # <class 'float'>
print(type(text))   # <class 'str'>
print(type(flag))   # <class 'bool'>


# ---------- 4. TYPE CASTING (CONVERTING TYPES) ----------
# Sometimes we need to convert one data type into another.

a = "10"
b = int(a)        # string to integer
print(b + 5)      # 15

c = 10
d = str(c)        # integer to string
print(d + "5")    # "105" (string joining, not addition)

e = "3.14"
f = float(e)      # string to float
print(f)

g = 7.9
h = int(g)        # float to int (decimal part is removed, NOT rounded)
print(h)          # 7


# ---------- 5. TAKING INPUT FROM USER ----------
# input() always returns a STRING, even if user types a number.

# Uncomment below lines to try in your own terminal:
# user_name = input("Enter your name: ")
# print("Hello,", user_name)

# user_age = input("Enter your age: ")
# user_age = int(user_age)     # convert string to int for calculations
# print("Next year you will be:", user_age + 1)


# ---------- 6. COMMENTS ----------
# This is a single-line comment

"""
This is a
multi-line comment
(also called a docstring when used at the top of a function/class)
"""


# ---------- 7. ID and MEMORY ----------
# id() gives the memory address of a variable (mostly for learning purpose)
x = 5
print(id(x))
