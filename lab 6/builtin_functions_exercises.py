import math
import time
import functools

def multiply_list(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

def is_palindrome(s):
    return s == s[::-1]

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

def all_true(t):
    return all(t)

# Example usage
if __name__ == "__main__":
    print("Product of list:", multiply_list([1, 2, 3, 4]))
    upper, lower = count_case("Hello World")
    print(f"Uppercase: {upper}, Lowercase: {lower}")
    print("Is palindrome:", is_palindrome("madam"))
    print(f"Square root of 25100 after 2123 milliseconds is {delayed_sqrt(25100, 2123)}")
    print("All elements true:", all_true((True, True, False)))
