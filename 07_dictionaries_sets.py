# =====================================================
# TOPIC 7: DICTIONARIES AND SETS
# Creation, Methods, Operations
# =====================================================

# =================== DICTIONARIES ===================
# A dictionary stores data as KEY-VALUE pairs.
# It is ORDERED (Python 3.7+), CHANGEABLE, and does NOT allow duplicate keys.

# ---------- 1. CREATING A DICTIONARY ----------
student = {
    "name": "Riya",
    "age": 21,
    "course": "Python"
}
print(student)


# ---------- 2. ACCESSING VALUES ----------
print(student["name"])         # Riya
print(student.get("age"))      # 21 (safer way, avoids error if key doesn't exist)
print(student.get("city", "Not Found"))   # default value if key is missing


# ---------- 3. MODIFYING / ADDING ITEMS ----------
student["age"] = 22            # update existing key
student["city"] = "Delhi"      # add a new key-value pair
print(student)


# ---------- 4. REMOVING ITEMS ----------
student.pop("city")            # removes a specific key
print(student)

# del student["age"]           # another way to delete a key
# student.clear()              # removes all items


# ---------- 5. LOOPING THROUGH A DICTIONARY ----------
for key in student:
    print(key, ":", student[key])

for key, value in student.items():   # .items() gives key-value pairs together
    print(key, "->", value)

for key in student.keys():     # only keys
    print(key)

for value in student.values():  # only values
    print(value)


# ---------- 6. USEFUL DICTIONARY METHODS ----------
print(len(student))             # number of key-value pairs
print("name" in student)        # True -> checks if key exists
print(student.keys())           # all keys
print(student.values())         # all values
print(student.items())          # all key-value pairs

student_copy = student.copy()    # creates a copy of the dictionary
print(student_copy)


# ---------- 7. DICTIONARY COMPREHENSION ----------
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ---------- 8. NESTED DICTIONARY ----------
students = {
    "student1": {"name": "Aman", "age": 20},
    "student2": {"name": "Priya", "age": 22}
}
print(students["student1"]["name"])    # Aman


# =================== SETS ===================
# A set is an UNORDERED collection that does NOT allow duplicate values.
# Sets are mainly used to store unique items and perform mathematical operations.

# ---------- 9. CREATING A SET ----------
my_set = {1, 2, 3, 3, 4}    # duplicates are automatically removed
print(my_set)                # {1, 2, 3, 4}


# ---------- 10. ADDING AND REMOVING ITEMS ----------
my_set.add(10)               # adds one item
print(my_set)

my_set.update([20, 30])      # adds multiple items
print(my_set)

my_set.remove(2)             # removes an item (error if not found)
print(my_set)

my_set.discard(100)          # removes an item safely (NO error if not found)
print(my_set)


# ---------- 11. SET OPERATIONS (Mathematical) ----------
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))            # all unique items from both -> {1,2,3,4,5,6}
print(a.intersection(b))     # common items in both       -> {3,4}
print(a.difference(b))       # items in 'a' but not in 'b' -> {1,2}
print(a.symmetric_difference(b))  # items NOT common in both -> {1,2,5,6}


# ---------- 12. CHECKING MEMBERSHIP ----------
print(3 in a)        # True
print(10 in a)       # False
