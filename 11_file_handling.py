# =====================================================
# TOPIC 11: FILE HANDLING
# Reading, Writing, Appending Files, 'with' statement
# =====================================================

# ---------- 1. FILE MODES ----------
# "r"  -> read (default mode, file must exist)
# "w"  -> write (creates new file OR overwrites existing file completely)
# "a"  -> append (adds data to the end, without deleting old content)
# "r+" -> read and write
# "x"  -> create a new file, fails if it already exists


# ---------- 2. WRITING TO A FILE ----------
# Using 'with' is the BEST practice -> it automatically closes the file after use

with open("sample.txt", "w") as file:
    file.write("Hello, this is my first line.\n")
    file.write("This is the second line.\n")

# Without 'with', you would need to manually close the file:
# file = open("sample.txt", "w")
# file.write("Hello")
# file.close()    # IMPORTANT - must always close manually if not using 'with'


# ---------- 3. READING A FILE (entire content) ----------
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)


# ---------- 4. READING A FILE LINE BY LINE ----------
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())    # strip() removes the extra newline character


# ---------- 5. READING ALL LINES INTO A LIST ----------
with open("sample.txt", "r") as file:
    lines = file.readlines()    # returns a list, each item is one line
    print(lines)


# ---------- 6. READING JUST ONE LINE ----------
with open("sample.txt", "r") as file:
    first_line = file.readline()
    print(first_line)


# ---------- 7. APPENDING TO A FILE ----------
# Adds new content WITHOUT deleting what's already there

with open("sample.txt", "a") as file:
    file.write("This is an appended line.\n")

with open("sample.txt", "r") as file:
    print(file.read())


# ---------- 8. CHECKING IF A FILE EXISTS (to avoid errors) ----------
import os

if os.path.exists("sample.txt"):
    print("File exists!")
else:
    print("File does not exist.")


# ---------- 9. HANDLING FILE ERRORS SAFELY ----------
try:
    with open("non_existing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file does not exist!")


# ---------- 10. DELETING A FILE ----------
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File deleted successfully.")
