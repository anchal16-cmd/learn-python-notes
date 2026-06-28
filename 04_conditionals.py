# =====================================================
# TOPIC 4: CONDITIONAL STATEMENTS
# if, elif, else, nested if, ternary operator
# =====================================================

# ---------- 1. SIMPLE IF STATEMENT ----------
age = 20

if age >= 18:
    print("You are an adult.")   # runs only if condition is True


# ---------- 2. IF-ELSE STATEMENT ----------
num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ---------- 3. IF-ELIF-ELSE LADDER ----------
# Used when there are multiple conditions to check one by one

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ---------- 4. NESTED IF (if inside another if) ----------
num = 15

if num > 0:
    if num % 2 == 0:
        print("Positive Even number")
    else:
        print("Positive Odd number")
else:
    print("Negative number")


# ---------- 5. SHORTHAND IF (TERNARY OPERATOR) ----------
# Useful for simple one-line conditions

age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)   # Minor


# ---------- 6. MULTIPLE CONDITIONS USING and / or ----------
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

# Using or
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It's a weekend!")
else:
    print("It's a weekday.")


# ---------- 7. pass STATEMENT ----------
# pass is used as a placeholder when a block is empty but syntax requires something

x = 10
if x > 5:
    pass   # Do nothing for now (useful while writing code structure first)
print("Code continues...")
