# Python Scope
# Explanation:
# Scope determines the visibility of variables within a program. Python has four types of scopes:

# Local Scope – Variables inside a function.
# Enclosing Scope – Variables in nested functions.
# Global Scope – Variables declared outside any function.
# Built-in Scope – Predefined names like print().
# Examples of Scope
# Local Scope

def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10

# Global Scope

x = 100  # Global variable

def my_function():
    print(x)

my_function()  # Output: 100

# Enclosing Scope

def outer():
    y = 20
    def inner():
        print(y)  # Accessing enclosing variable
    inner()

outer()  # Output: 20


# Using global Keyword

x = 5

def modify_global():
    global x
    x = 10

modify_global()
print(x)  # Output: 10
