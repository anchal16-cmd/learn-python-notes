# =====================================================
# TOPIC 12: MODULES, IMPORTS & MISCELLANEOUS
# Modules, datetime, useful built-in functions, misc concepts
# =====================================================

# ---------- 1. WHAT IS A MODULE? ----------
# A module is simply a Python file (.py) containing functions/classes/variables
# that you can reuse in other programs using 'import'.


# ---------- 2. IMPORTING A BUILT-IN MODULE ----------
import math

print(math.sqrt(25))      # 5.0  -> square root
print(math.pow(2, 3))     # 8.0  -> power
print(math.pi)            # 3.14159...
print(math.floor(4.7))    # 4    -> rounds down
print(math.ceil(4.2))     # 5    -> rounds up


# ---------- 3. IMPORTING SPECIFIC FUNCTIONS ----------
from math import sqrt, pi
print(sqrt(16))    # 4.0
print(pi)


# ---------- 4. IMPORT WITH ALIAS ----------
import math as m
print(m.sqrt(36))   # 6.0


# ---------- 5. RANDOM MODULE ----------
import random

print(random.randint(1, 10))      # random integer between 1 and 10 (inclusive)
print(random.random())             # random float between 0.0 and 1.0
fruits = ["apple", "banana", "mango"]
print(random.choice(fruits))       # randomly picks one item from the list
random.shuffle(fruits)             # shuffles the list in place
print(fruits)


# ---------- 6. DATETIME MODULE ----------
import datetime

now = datetime.datetime.now()
print(now)                  # current date and time
print(now.year)             # current year
print(now.month)            # current month
print(now.day)               # current day
print(now.strftime("%d-%m-%Y"))   # formats date as dd-mm-yyyy
print(now.strftime("%H:%M:%S"))   # formats time as HH:MM:SS


# ---------- 7. USEFUL BUILT-IN FUNCTIONS ----------
nums = [4, 2, 9, 1, 7]

print(len(nums))       # length of list -> 5
print(max(nums))       # largest value  -> 9
print(min(nums))       # smallest value -> 1
print(sum(nums))       # sum of all     -> 23
print(sorted(nums))    # returns a NEW sorted list (original unchanged)
print(round(3.567, 2)) # rounds to 2 decimal places -> 3.57
print(abs(-10))         # absolute value -> 10

# zip() - combines multiple lists element-wise
names = ["Aman", "Riya"]
scores = [85, 90]
combined = list(zip(names, scores))
print(combined)         # [('Aman', 85), ('Riya', 90)]

# enumerate() - adds index to an iterable
for index, name in enumerate(names):
    print(index, name)


# ---------- 8. MAP, FILTER, REDUCE ----------
from functools import reduce

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, nums))      # apply function to all items
print(squared)         # [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, nums)) # keep only items matching condition
print(evens)            # [2, 4]

total = reduce(lambda a, b: a + b, nums)         # combine all items into one value
print(total)             # 15


# ---------- 9. CREATING YOUR OWN MODULE ----------
# Save this code in a file called 'mymodule.py':
#
#   def greet(name):
#       return f"Hello, {name}!"
#
# Then in another file, you can use it like this:
#
#   import mymodule
#   print(mymodule.greet("Aman"))


# ---------- 10. THE __name__ == "__main__" CHECK ----------
# This ensures certain code runs ONLY when the file is executed directly,
# NOT when it is imported into another file.

def main():
    print("This runs only when the file is executed directly.")

if __name__ == "__main__":
    main()
