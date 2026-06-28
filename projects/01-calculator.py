# Python program to create a multi-feature calculator
# Performs basic arithmetic operations and calculates area of different shapes

# Step 1: Print the main menu showing available options to the user
print("===== CALCULATOR =====")
print("1. Arithmetic Calculator")
print("2. Area Calculator")
print("3. Exit")

# Step 2: Take user's choice as input (1, 2, or 3)
choice = int(input("Enter your choice (1/2/3): "))

# Step 3: If user chooses Arithmetic Calculator, show arithmetic sub-menu and perform the selected operation (+, -, *, /)
if choice == 1:
    print("\n--- Arithmetic Calculator ---")
    print("a. Addition (+)")
    print("b. Subtraction (-)")
    print("c. Multiplication (*)")
    print("d. Division (/)")

    operation = input("Enter operation (a/b/c/d): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "a":
        print("Result:", num1 + num2)
    elif operation == "b":
        print("Result:", num1 - num2)
    elif operation == "c":
        print("Result:", num1 * num2)
    elif operation == "d":
        print("Result:", num1 / num2)
    else:
        print("Invalid operation selected!")

# Step 4: If user chooses Area Calculator, show shapes sub-menu and calculate area based on the selected shape
elif choice == 2:
    print("\n--- Area Calculator ---")
    print("a. Circle")
    print("b. Rectangle")
    print("c. Triangle")
    print("d. Square")

    shape = input("Enter shape (a/b/c/d): ")

    if shape == "a":
        radius = float(input("Enter radius: "))
        area = 3.14 * radius * radius
        print("Area of Circle:", area)

    elif shape == "b":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print("Area of Rectangle:", area)

    elif shape == "c":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of Triangle:", area)

    elif shape == "d":
        side = float(input("Enter side: "))
        area = side * side
        print("Area of Square:", area)

    else:
        print("Invalid shape selected!")

# Step 5: If user chooses Exit, end the program
elif choice == 3:
    print("Exiting the calculator. Goodbye!")
else:
    print("Invalid choice! Please select 1, 2, or 3.")

# Step 6: Repeat the whole process using a loop, so the user can use the calculator multiple times without restarting the program

# Python program to create a multi-feature calculator
# Performs basic arithmetic operations and calculates area of different shapes

# Step 6: Repeat the whole process using a loop, so the user can use the calculator multiple times without restarting the program
while True:

    # Step 1: Print the main menu showing available options to the user
    print("\n===== CALCULATOR =====")
    print("1. Arithmetic Calculator")
    print("2. Area Calculator")
    print("3. Exit")

    # Step 2: Take user's choice as input (1, 2, or 3)
    choice = int(input("Enter your choice (1/2/3): "))

    # Step 3: If user chooses Arithmetic Calculator, show arithmetic sub-menu
    #         and perform the selected operation (+, -, *, /)
    if choice == 1:
        print("\n--- Arithmetic Calculator ---")
        print("a. Addition (+)")
        print("b. Subtraction (-)")
        print("c. Multiplication (*)")
        print("d. Division (/)")

        operation = input("Enter operation (a/b/c/d): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "a":
            print("Result:", num1 + num2)
        elif operation == "b":
            print("Result:", num1 - num2)
        elif operation == "c":
            print("Result:", num1 * num2)
        elif operation == "d":
            print("Result:", num1 / num2)
        else:
            print("Invalid operation selected!")

    # Step 4: If user chooses Area Calculator, show shapes sub-menu
    #         and calculate area based on the selected shape
    elif choice == 2:
        print("\n--- Area Calculator ---")
        print("a. Circle")
        print("b. Rectangle")
        print("c. Triangle")
        print("d. Square")

        shape = input("Enter shape (a/b/c/d): ")

        if shape == "a":
            radius = float(input("Enter radius: "))
            area = 3.14159 * radius * radius
            print("Area of Circle:", area)
        elif shape == "b":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print("Area of Rectangle:", area)
        elif shape == "c":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print("Area of Triangle:", area)
        elif shape == "d":
            side = float(input("Enter side: "))
            area = side * side
            print("Area of Square:", area)
        else:
            print("Invalid shape selected!")

    # Step 5: If user chooses Exit, end the program
    elif choice == 3:
        print("Exiting the calculator. Goodbye!")
        break    # this stops the while loop completely

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
