
### **1. Convert Degree to Radian**

import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

# Input
degree = float(input("Input degree: "))
radian = degree_to_radian(degree)

# Output
print("Output radian:", round(radian, 6))

#### **Example Run**

# Input degree: 15
# Output radian: 0.261799


### **2. Calculate the Area of a Trapezoid**

def trapezoid_area(base1, base2, height):
    return ((base1 + base2) * height) / 2

# Input
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

# Output
print("Expected Output:", trapezoid_area(base1, base2, height))

#### **Example Run**

# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5


### **3. Calculate the Area of a Regular Polygon**

import math

def regular_polygon_area(n, s):
    return (n * s**2) / (4 * math.tan(math.pi / n))

# Input
num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

# Output
print("The area of the polygon is:", round(regular_polygon_area(num_sides, side_length), 2))

#### **Example Run**

# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625.0


### **4. Calculate the Area of a Parallelogram**


def parallelogram_area(base, height):
    return base * height

# Input
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

# Output
print("Expected Output:", parallelogram_area(base, height))

#### **Example Run**

# Length of base: 5
# Height of parallelogram: 6
# Expected Output: 30.0

