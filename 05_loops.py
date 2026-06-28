# =====================================================
# TOPIC 5: LOOPS IN PYTHON
# for loop, while loop, break, continue, nested loops
# =====================================================

# ---------- 1. FOR LOOP ----------
# Used when we know how many times to repeat (iterate over a sequence)

for i in range(5):     # range(5) -> 0,1,2,3,4
    print(i)

# range(start, stop, step)
for i in range(2, 10, 2):    # 2,4,6,8 (10 is excluded)
    print(i)


# ---------- 2. LOOPING THROUGH A LIST/STRING ----------
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

for char in "Python":
    print(char)


# ---------- 3. WHILE LOOP ----------
# Used when we don't know in advance how many times to repeat,
# it runs as long as the condition is True

count = 1
while count <= 5:
    print("Count:", count)
    count += 1   # IMPORTANT: always update the variable, else infinite loop!


# ---------- 4. BREAK STATEMENT ----------
# Stops/exits the loop completely

for i in range(10):
    if i == 5:
        break    # loop stops as soon as i becomes 5
    print(i)     # prints 0,1,2,3,4


# ---------- 5. CONTINUE STATEMENT ----------
# Skips the current iteration and moves to the next one

for i in range(10):
    if i % 2 == 0:
        continue   # skip even numbers
    print(i)       # prints only odd numbers: 1,3,5,7,9


# ---------- 6. ELSE WITH LOOPS ----------
# The else block runs ONLY if the loop completes without a 'break'

for i in range(5):
    print(i)
else:
    print("Loop finished without break")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will NOT print because loop was broken")


# ---------- 7. NESTED LOOPS ----------
# A loop inside another loop (useful for patterns, grids, etc.)

for i in range(1, 4):           # outer loop
    for j in range(1, 4):       # inner loop
        print(f"i={i}, j={j}")


# ---------- 8. SIMPLE PATTERN PRINTING USING LOOPS ----------
# A classic beginner exercise: printing a triangle pattern

rows = 5
for i in range(1, rows + 1):
    print("*" * i)

# Output:
# *
# **
# ***
# ****
# *****
