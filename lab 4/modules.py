# Python Modules
# Explanation:
# A module is a file containing Python code that can be reused. It can define functions, classes, and variables.

# Built-in modules: math, random, json, etc.
# Custom modules: User-defined .py files.
# Importing modules: import module_name, from module_name import function_name.
# Examples of Using Modules
# Importing a Module

import math
print(math.sqrt(16))  # Output: 4.0
# Using from Keyword

from math import factorial
print(factorial(5))  # Output: 120
# Creating a Custom Module (mymodule.py)

def greet(name):
    return f"Hello, {name}!"


# Importing the module:

# import my_module
# print(my_module.greet("Alice"))  # Output: Hello, Alice!


# Using dir() to List Module Contents

import math
print(dir(math))  # Lists all functions in math module
