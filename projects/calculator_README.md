# 🧮 Multi-Feature Calculator (Python)

A simple, menu-driven calculator built in Python. It lets the user choose between performing basic arithmetic operations or calculating the area of different shapes — all from one program that keeps running until the user chooses to exit.

---

## ✨ Features

**1. Arithmetic Calculator**
- Addition (+)
- Subtraction (−)
- Multiplication (×)
- Division (÷)

**2. Area Calculator**
- Circle
- Rectangle
- Triangle
- Square

**3. Exit**
- Cleanly ends the program when the user is done

---

## 🛠️ How It Works

1. The program displays a main menu with three options.
2. The user enters a choice (`1`, `2`, or `3`).
3. Based on the choice:
   - **Arithmetic Calculator** → asks for an operation and two numbers, then prints the result.
   - **Area Calculator** → asks for a shape and its dimensions, then prints the area.
   - **Exit** → prints a goodbye message and stops the program.
4. After completing a calculation, the menu appears again automatically (thanks to a `while` loop), so the user can perform multiple calculations without restarting the program.

---

## 🚀 How to Run

```bash
python calculator.py
```

Then follow the on-screen prompts:

```
===== CALCULATOR =====
1. Arithmetic Calculator
2. Area Calculator
3. Exit
Enter your choice (1/2/3):
```

---

## 📋 Example Run

```
===== CALCULATOR =====
1. Arithmetic Calculator
2. Area Calculator
3. Exit
Enter your choice (1/2/3): 2

--- Area Calculator ---
a. Circle
b. Rectangle
c. Triangle
d. Square
Enter shape (a/b/c/d): a
Enter radius: 7
Area of Circle: 153.93791

===== CALCULATOR =====
1. Arithmetic Calculator
2. Area Calculator
3. Exit
Enter your choice (1/2/3): 3
Exiting the calculator. Goodbye!
```

---

## 🧠 Concepts Used

This project applies several core Python concepts in one place:

- `input()` and type conversion (`int()`, `float()`)
- `if` / `elif` / `else` conditional logic
- Nested conditionals (sub-menus inside the main menu)
- `while` loop for repeated execution
- `break` statement to exit the loop
- Basic arithmetic and geometry formulas

---

## 📌 Note

This project was built as part of my Python learning journey, applying concepts from variables, conditionals, and loops in a single hands-on program.
