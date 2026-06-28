# =====================================================
# TOPIC 3: STRINGS IN PYTHON
# Creation, Indexing, Slicing, Methods, Formatting
# =====================================================

# ---------- 1. CREATING STRINGS ----------
s1 = 'Hello'
s2 = "World"
s3 = '''This is a
multi-line string'''

print(s1, s2)
print(s3)


# ---------- 2. STRING INDEXING ----------
# Each character has a position (index), starting from 0
# Negative index counts from the end (-1 is the last character)

word = "Python"
print(word[0])    # P  (first character)
print(word[5])    # n  (last character)
print(word[-1])   # n  (last character, using negative index)
print(word[-6])   # P  (first character, using negative index)


# ---------- 3. STRING SLICING ----------
# Syntax: string[start:stop:step]  -> stop index is NOT included

print(word[0:4])    # Pyth   (index 0 to 3)
print(word[2:])     # thon   (from index 2 to end)
print(word[:4])     # Pyth   (from start to index 3)
print(word[::-1])   # nohtyP (reverses the string)
print(word[::2])    # Pto    (every 2nd character)


# ---------- 4. STRING CONCATENATION & REPETITION ----------
first = "Hello"
second = "Python"

print(first + " " + second)   # Joining strings -> Hello Python
print(first * 3)              # Repeating string -> HelloHelloHello


# ---------- 5. COMMON STRING METHODS ----------
text = "  Hello Python World  "

print(text.upper())         # Converts to uppercase
print(text.lower())         # Converts to lowercase
print(text.strip())         # Removes leading/trailing spaces
print(text.replace("Python", "Java"))   # Replaces a substring
print(text.split())         # Splits into a list of words by space
print(len(text))            # Length of the string (including spaces)
print(text.find("Python"))  # Returns starting index of substring (-1 if not found)
print(text.count("o"))      # Counts occurrences of a character/substring
print("python".capitalize())  # Capitalizes first letter -> Python
print("Python".startswith("Py"))  # True
print("Python".endswith("on"))    # True
print("123".isdigit())      # True -> checks if all characters are digits
print("abc".isalpha())      # True -> checks if all characters are letters


# ---------- 6. STRING FORMATTING ----------
name = "Aman"
age = 21

# Method 1: f-strings (recommended, most used in modern Python)
print(f"My name is {name} and I am {age} years old.")

# Method 2: .format()
print("My name is {} and I am {} years old.".format(name, age))

# Method 3: % operator (older style)
print("My name is %s and I am %d years old." % (name, age))


# ---------- 7. STRING IS IMMUTABLE ----------
# Once created, a string's characters CANNOT be changed directly.
s = "Hello"
# s[0] = "J"   # This will give an ERROR because strings are immutable
s = "Jello"    # Instead, you must create a new string
print(s)


# ---------- 8. LOOPING THROUGH A STRING ----------
for char in "abc":
    print(char)   # prints each character one by one
