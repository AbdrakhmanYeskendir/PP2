### **1. Generator to Generate Squares of Numbers up to N**

def generate_squares(n):
    for i in range(n + 1):
        yield i ** 2  # Yield square of each number

# Example usage
n = 5
for square in generate_squares(n):
    print(square, end=" ")  # Output: 0 1 4 9 16 25


### **2. Generator to Print Even Numbers up to N (Comma-Separated)**

def even_numbers(n):
    for i in range(0, n + 1, 2):  # Step by 2 for even numbers
        yield i

# Get user input
n = int(input("Enter a number: "))

# Generate even numbers and join them with commas
print(",".join(map(str, even_numbers(n))))

#### **Example Input & Output**

# Enter a number: 10
# 0,2,4,6,8,10


### **3. Generator for Numbers Divisible by 3 and 4 up to N**

def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage
n = 50
print(list(divisible_by_3_and_4(n)))  # Output: [0, 12, 24, 36, 48]


### **4. Generator to Yield Squares from `a` to `b`**

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Example usage
for sq in squares(3, 7):
    print(sq)  

#### **Output**

9
16
25
36
49


### **5. Generator to Yield Numbers from `n` Down to `0`**

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Example usage
n = 5
for num in countdown(n):
    print(num, end=" ")  # Output: 5 4 3 2 1 0



