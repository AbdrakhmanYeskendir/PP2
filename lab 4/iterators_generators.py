# Python Iterators
# Explanation:
# An iterator in Python is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__(). An iterable is an object that can return an iterator, meaning it implements the __iter__() method.

# The iter() function is used to get an iterator from an iterable.
# The next() function is used to retrieve the next item from an iterator.
# Once there are no more items, StopIteration is raised.
# Examples of Iterators
# Using iter() and next()

numbers = [1, 2, 3, 4]
iterator = iter(numbers)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2


# Creating a Custom Iterator

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

counter = Counter(5)
for num in counter:
    print(num)  # Output: 1, 2, 3, 4, 5

# Using Iterators with for Loop

my_list = [10, 20, 30, 40]
my_iter = iter(my_list)

for item in my_iter:
    print(item)  # Output: 10, 20, 30, 40


# Iterator with __next__() in a Class


class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.text[self.index]

rev = ReverseString("Python")


for char in rev:
    print(char)  # Output: n, o, h, t, y, P
# Python Generators
# Explanation:
# A generator is a special type of iterator that allows you to yield values one by one instead of returning them all at once. It is defined using a function with the yield keyword.

# Generators are memory efficient because they generate values on the fly.
# The state of the function is preserved between yield calls.
# Examples of Generators
# Simple Generator

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
# Generator for Fibonacci Sequence

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)  # Output: 0, 1, 1, 2, 3


# Generator for Infinite Sequence


def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1

counter = infinite_counter()
print(next(counter))  # Output: 0
print(next(counter))  # Output: 1


# Using yield in a Generator to Read Large Files

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

for line in read_large_file("data.txt"):
    print(line)
