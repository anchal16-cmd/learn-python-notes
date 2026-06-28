# =====================================================
# TOPIC 2: OPERATORS IN PYTHON
# Arithmetic, Comparison, Logical, Assignment, Bitwise
# =====================================================

# ---------- 1. ARITHMETIC OPERATORS ----------
a = 10
b = 3

print(a + b)    # Addition       -> 13
print(a - b)    # Subtraction    -> 7
print(a * b)    # Multiplication -> 30
print(a / b)    # Division (gives float)        -> 3.333...
print(a // b)   # Floor Division (removes decimal) -> 3
print(a % b)    # Modulus (remainder)            -> 1
print(a ** b)   # Exponent (power)               -> 1000


# ---------- 2. COMPARISON (RELATIONAL) OPERATORS ----------
# These always return True or False

print(a == b)   # Equal to            -> False
print(a != b)   # Not equal to        -> True
print(a > b)    # Greater than        -> True
print(a < b)    # Less than           -> False
print(a >= b)   # Greater or equal    -> True
print(a <= b)   # Less or equal       -> False


# ---------- 3. LOGICAL OPERATORS ----------
# Used to combine conditional statements

x = True
y = False

print(x and y)   # True only if BOTH are True   -> False
print(x or y)    # True if AT LEAST ONE is True -> True
print(not x)     # Reverses the value           -> False


# ---------- 4. ASSIGNMENT OPERATORS ----------
# Used to assign and update values quickly

num = 5
num += 3   # same as num = num + 3   -> 8
print(num)

num -= 2   # same as num = num - 2   -> 6
print(num)

num *= 4   # same as num = num * 4   -> 24
print(num)

num /= 3   # same as num = num / 3   -> 8.0
print(num)

num //= 2  # same as num = num // 2
print(num)

num **= 2  # same as num = num ** 2
print(num)

num %= 5   # same as num = num % 5
print(num)


# ---------- 5. BITWISE OPERATORS ----------
# Work on the binary form of numbers (advanced, but good to know)

p = 5   # binary: 0101
q = 3   # binary: 0011

print(p & q)    # AND  -> 1   (bitwise AND)
print(p | q)    # OR   -> 7   (bitwise OR)
print(p ^ q)    # XOR  -> 6   (bitwise XOR)
print(~p)       # NOT  -> -6  (inverts all bits)
print(p << 1)   # Left shift  -> 10 (multiplies by 2)
print(p >> 1)   # Right shift -> 2  (divides by 2)


# ---------- 6. MEMBERSHIP OPERATORS ----------
# Used to check if a value exists inside a sequence (list, string, etc.)

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)       # True
print("grapes" not in fruits)  # True


# ---------- 7. IDENTITY OPERATORS ----------
# Used to compare memory location of two objects (not just value)

m = [1, 2, 3]
n = [1, 2, 3]
o = m

print(m is n)       # False -> different objects in memory, even if same values
print(m is o)       # True  -> o points to the same object as m
print(m == n)       # True  -> values are equal (== checks value, not identity)
