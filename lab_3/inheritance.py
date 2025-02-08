# Inheritance in Python is a fundamental object-oriented programming 
# concept that allows a class (called the **child** or **subclass**) to 
# inherit properties and behaviors (attributes and methods) from another class 
# (called the **parent** or **base class**). This promotes code reuse and establishes a relationship between classes.

# ### Key Points

# 1. **Basic Syntax**:
   
class Parent:
    def show(self):
        print("This is the parent class.")

class Child(Parent):  # Child inherits from Parent
    def display(self):
        print("This is the child class.")
   

# 2. **Accessing Parent Methods**:
#    - The child class can use methods defined in the parent class:

c = Child()
c.show()     # Output: This is the parent class.
c.display()  # Output: This is the child class.
   

# 3. **Method Overriding**:
#    - The child class can provide its own implementation of a method inherited from the parent:

class Child(Parent):
    def show(self):  # Overriding
       print("This is the overridden method in the child class.")


# 4. **Benefits**:
#    - Code Reusability: Reduces redundancy by allowing shared code.
#    - Base Class Functionality: Child classes can extend or customize the behavior of parent classes.

### Summary

# Inheritance allows for a hierarchical organization of classes, facilitating the use of shared code and the creation of more complex data structures while keeping the codebase clean and maintainable.
