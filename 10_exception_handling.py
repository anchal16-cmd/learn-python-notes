# =====================================================
# TOPIC 10: EXCEPTION HANDLING
# try, except, else, finally, raise, custom exceptions
# =====================================================

# ---------- 1. WHY EXCEPTION HANDLING? ----------
# Without handling, errors STOP the entire program.
# Example (uncommenting below will crash the program):
# print(10 / 0)    # ZeroDivisionError

# Exception handling lets us catch errors and continue running the program.


# ---------- 2. BASIC TRY-EXCEPT ----------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")


# ---------- 3. HANDLING MULTIPLE EXCEPTIONS ----------
try:
    num = int("abc")    # this will cause a ValueError
except ZeroDivisionError:
    print("Division error")
except ValueError:
    print("Error: Invalid value, cannot convert to integer")


# ---------- 4. CATCHING ANY EXCEPTION (generic) ----------
try:
    x = 10 / 0
except Exception as e:       # catches ANY type of error
    print("Something went wrong:", e)


# ---------- 5. ELSE WITH TRY-EXCEPT ----------
# The else block runs ONLY IF no exception occurred

try:
    num = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful, result is:", num)


# ---------- 6. FINALLY BLOCK ----------
# finally ALWAYS runs, whether an exception occurred or not
# Useful for cleanup tasks like closing files or connections

try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always run, no matter what.")


# ---------- 7. RAISING YOUR OWN EXCEPTION ----------
# 'raise' is used to manually trigger an exception

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Valid age:", age)

try:
    check_age(-5)
except ValueError as e:
    print("Caught an error:", e)


# ---------- 8. CUSTOM EXCEPTIONS ----------
# You can create your own exception classes by inheriting from Exception

class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance for this withdrawal!")
    return balance - amount

try:
    new_balance = withdraw(1000, 1500)
except InsufficientBalanceError as e:
    print("Transaction failed:", e)


# ---------- 9. COMMON BUILT-IN EXCEPTIONS (good to know) ----------
# ZeroDivisionError   -> dividing by zero
# ValueError          -> invalid value for conversion (e.g. int("abc"))
# TypeError           -> wrong data type used in an operation
# IndexError          -> list index out of range
# KeyError            -> dictionary key not found
# FileNotFoundError   -> file does not exist
# NameError           -> using a variable that hasn't been defined

try:
    my_list = [1, 2, 3]
    print(my_list[10])   # IndexError - index doesn't exist
except IndexError:
    print("Error: List index is out of range!")
