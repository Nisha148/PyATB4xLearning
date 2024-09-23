"""Task #3
- Explain the difference between the = operator and the == operator in Python.

- What does the ** operator do in Python, and how is it used?

- What does the ^ operator do in Python, and in what context is it commonly used?
"""
import math
import operator

from src.ex_17082024.Lab032 import radius

# Task 3

# = -> is a assignment operator, ==is a comparison operator.
# ** is used for power, it can be use like (2 ** 3 ) o/p =8 , 2*2*2
# ^ is a XOR operator,(X^Y)

### Task #4
# - Write a Python program to calculate the area of a circle given its radius using the formula ``` area=π×r^2``` ( Take pie as 3.14)

# radius=float(input("Enter the radius\n"))
# print(radius)
# radius=math.pi*math.pow(radius,2)
# print("Radius= ",radius)

### Task #5
# - Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1 = input("Enter the number1\n")
num2 = input("Enter the number2\n")
print(num1 > num2)
print(num1 < num2)
print(num1 == num2)

# Task 6

import math

value=int(input("Enter the value"))
print(value)
square=math.sqrt(value)
print(square)
cube=math.cbrt(value)
print(cube)