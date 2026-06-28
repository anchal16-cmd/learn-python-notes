# =====================================================
# TOPIC 8: FUNCTIONS IN PYTHON
# Definition, Parameters, *args/**kwargs, Lambda, Recursion, Scope
# =====================================================

# ---------- 1. DEFINING AND CALLING A FUNCTION ----------
def greet():
    print("Hello, welcome to Python!")

greet()    # calling the function


# ---------- 2. FUNCTION WITH PARAMETERS ----------
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Aman")


# ---------- 3. FUNCTION WITH RETURN VALUE ----------
def add(a, b):
    return a + b      # return sends the result back to the caller

result = add(5, 10)
print(result)          # 15


# ---------- 4. DEFAULT PARAMETERS ----------
# If no value is passed, the default value is used

def greet_default(name="Guest"):
    print(f"Hello, {name}!")

greet_default()             # Hello, Guest!
greet_default("Riya")       # Hello, Riya!


# ---------- 5. KEYWORD ARGUMENTS ----------
# You can pass arguments by name, in any order

def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=21, name="Aman")    # order doesn't matter with keyword args


# ---------- 6. *args (Variable Number of Positional Arguments) ----------
# Used when we don't know how many arguments will be passed

def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add_all(1, 2, 3))         # 6
print(add_all(5, 10, 15, 20))   # 50


# ---------- 7. **kwargs (Variable Number of Keyword Arguments) ----------
# Collects extra named arguments into a dictionary

def show_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_details(name="Aman", age=21, course="Python")


# ---------- 8. LAMBDA FUNCTIONS (Anonymous Functions) ----------
# A short, one-line function without a name, defined using 'lambda'

square = lambda x: x ** 2
print(square(5))    # 25

add_lambda = lambda a, b: a + b
print(add_lambda(3, 4))   # 7

# Commonly used with map(), filter(), sorted()
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, nums))
print(squared)        # [1, 4, 9, 16, 25]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)           # [2, 4]


# ---------- 9. RECURSION (Function calling itself) ----------
def factorial(n):
    if n == 0 or n == 1:    # base case - stops the recursion
        return 1
    else:
        return n * factorial(n - 1)   # function calls itself

print(factorial(5))    # 120 (5*4*3*2*1)


# ---------- 10. VARIABLE SCOPE (Local vs Global) ----------
global_var = "I am global"   # accessible everywhere in the file

def show_scope():
    local_var = "I am local"    # accessible only inside this function
    print(global_var)            # can access global variable
    print(local_var)

show_scope()
# print(local_var)   # This will cause an ERROR - local_var doesn't exist outside the function


# To MODIFY a global variable inside a function, use the 'global' keyword
counter = 0

def increase_counter():
    global counter
    counter += 1

increase_counter()
increase_counter()
print(counter)    # 2


# ---------- 11. DOCSTRINGS (Function Documentation) ----------
def multiply(a, b):
    """This function takes two numbers and returns their product."""
    return a * b

print(multiply(4, 5))     # 20
print(multiply.__doc__)   # prints the docstring
