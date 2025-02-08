# 1. String Manipulation Class

class StringManipulator:  
    def getString(self):  
        self.input_string = input("Enter a string: ")  

    def printString(self):  
        print(self.input_string.upper())  
# 2. Shape and Square Classes

class Shape:  
    def area(self):  
        return 0  

class Square(Shape):  
    def __init__(self, length):  
        self.length = length  

    def area(self):  
        return self.length ** 2  
# 3. Rectangle Class

class Rectangle(Shape):  
    def __init__(self, length, width):  
        self.length = length  
        self.width = width  

    def area(self):  
        return self.length * self.width  
    

# Example of using these codes( #2,3 )
# Create a square with length 4  
square = Square(4)  
print(square.area())  # Output: 16 (4^2)  

# Create a rectangle with length 5 and width 3  
rectangle = Rectangle(5, 3)  
print(rectangle.area())  # Output: 15 (5 * 3)  



# 4. Point Class

import math  

class Point:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  

    def show(self):  
        print(f"Point coordinates: ({self.x}, {self.y})")  

    def move(self, x, y):  
        self.x += x  
        self.y += y  

    def dist(self, other):  
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)  
# 5. Bank Account Class

class Account:  
    def __init__(self, owner, balance=0):  
        self.owner = owner  
        self.balance = balance  

    def deposit(self, amount):  
        self.balance += amount  
        print(f"Deposited: ${amount}. New balance: ${self.balance}")  

    def withdraw(self, amount):  
        if amount <= self.balance:  
            self.balance -= amount  
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")  
        else:  
            print("Insufficient balance.")  
# Example of usage
# Creating an instance of the Account class  
account1 = Account("Alice", 1000)  

# Display the account owner and initial balance  
print(f"Account owner: {account1.owner}")  
print(f"Initial balance: ${account1.balance}")  

# Deposit money into the account  
account1.deposit(200)  # Expected output: "Deposited: $200. New balance: $1200"  

# Withdraw money from the account  
account1.withdraw(500)  # Expected output: "Withdrew: $500. New balance: $700"  

# Trying to withdraw more than the current balance  
account1.withdraw(800)  # Expected output: "Insufficient balance."  


# Expacted output:

# Account owner: Alice  
# Initial balance: $1000  
# Deposited: $200. New balance: $1200  
# Withdrew: $500. New balance: $700  
# Insufficient balance.  





# 6. Prime Number Filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

# A function to check if a number is prime  
is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))  

# Filtering prime numbers  
prime_numbers = list(filter(is_prime, numbers))  
print(f"Prime numbers: {prime_numbers}")  


# Example of Using the Classes:


# Using StringManipulator  
str_manipulator = StringManipulator()  
str_manipulator.getString()  
str_manipulator.printString()  

# Using Shape and Square  
square = Square(5)  
print(f"Area of square: {square.area()}")  

# Using Rectangle  
rectangle = Rectangle(4, 6)  
print(f"Area of rectangle: {rectangle.area()}")  

# Using Point  
point1 = Point(2, 3)  
point1.show()  
point1.move(1, -1)  
point1.show()  

point2 = Point(4, 5)  
distance = point1.dist(point2)  
print(f"Distance between points: {distance}")  

# Using Account  
account = Account("Alice", 100)  
account.deposit(50)  
account.withdraw(30)  
account.withdraw(150)  # Should show insufficient balance  

# Filter prime numbers  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
prime_numbers = list(filter(is_prime, numbers))  
print(f"Prime numbers: {prime_numbers}")  