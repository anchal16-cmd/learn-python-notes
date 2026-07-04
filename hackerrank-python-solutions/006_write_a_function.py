# HackerRank Problem: Write a Function (Leap Year)
# Difficulty: Medium
# Concepts Used: Functions, Conditional Statements, Modulus Operator

# Function to check whether a given year is a leap year
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
       if year % 100 == 0:
          if year % 400 == 0:
              leap = True
              
              
    return leap
    
    
year = int(input())
print(is_leap(year))