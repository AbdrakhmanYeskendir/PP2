import random  
import math  

# Task 1: Convert grams to ounces  
def grams_to_ounces(grams):  
    return 28.3495231 * grams  

# Task 2: Convert Fahrenheit to Centigrade  
def fahrenheit_to_centigrade(fahrenheit):  
    return (5 / 9) * (fahrenheit - 32)  

# Task 3: Solve the chicken and rabbit puzzle  
def solve(numheads, numlegs):  
    chickens = ( 4 * numheads - numlegs) // 2  
    rabbits = numheads - chickens  
    return chickens, rabbits  

# Task 4: Filter prime numbers  
def is_prime(num):  
    if num <= 1:  
        return False  
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:  
            return False  
    return True  

def filter_prime(numbers):  
    return [num for num in numbers if is_prime(num)]  

# Task 5: Print all permutations of a string  
def string_permutations(s):  
    from itertools import permutations  
    return [''.join(p) for p in permutations(s)]  

# Task 6: Reverse words in a sentence  
def reverse_sentence(sentence):  
    return ' '.join(sentence.split()[::-1])  

# Task 7: Check for 3 next to 3  
def has_33(nums):  
    for i in range(len(nums) - 1):  
        if nums[i] == 3 and nums[i + 1] == 3:  
            return True  
    return False  

# Task 8: Check for 007 in order  
def spy_game(nums):  
    sequence = [0, 0, 7]  
    seq_index = 0  
    for num in nums:  
        if num == sequence[seq_index]:  
            seq_index += 1  
            if seq_index == 3:  
                return True  
    return False  

# Task 9: Compute volume of a sphere  
def volume_of_sphere(radius):  
    return (4/3) * math.pi * (radius ** 3)  

# Task 10: Unique elements from a list  
def unique_elements(lst):  
    unique_lst = []  
    for elem in lst:  
        if elem not in unique_lst:  
            unique_lst.append(elem)  
    return unique_lst  

# Task 11: Check if a string is a palindrome  
def is_palindrome(s):  
    s = ''.join(filter(str.isalnum, s)).lower()  # Clean the string  
    return s == s[::-1]  

# For example, if s were "A man, a plan, a canal: Panama!", 
# the filtered result would be ['A', 'm', 'a', 'n', 'a', 'p', 'l', 
# 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'P', 'a', 'n', 'a', 'm', 'a'],
# and ''.join(...) would produce 'AmanaplanacanalPanama'.

# Task 12: Print a histogram  
def histogram(lst):  
    for i in lst:  
        print('*' * i)  

# Task 13: Guess the Number Game  
def guess_the_number():  
    name = input("Hello! What is your name? ")  
    secret_number = random.randint(1, 20)  
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")  
    
    guesses = 0  
    while True:  
        guess = int(input("Take a guess: "))  
        guesses += 1  
        if guess < secret_number:  
            print("Your guess is too low.")  
        elif guess > secret_number:  
            print("Your guess is too high.")  
        else:  
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")  
            break