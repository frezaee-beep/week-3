import seaborn as sns
import pandas as pd


# update/add code below ...
#Excercise 1: Write a function that takes an integer n as input and returns the nth Fibonacci number. The Fibonacci sequence is defined as follows: 

def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

# Excercise 2: Write a function that takes a list of integers as input and returns a new list containing only the even numbers from the original list.

def to_binary(n):
    if n < 2:
        return str(n)

    return to_binary(n // 2) + str(n % 2)
# Excercise 3:

def matching_brackets(sequence):
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in sequence:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack:
                return False

            if stack.pop() != pairs[char]:
                return False

    return len(stack) == 0
from functools import reduce


# Excercise 4: 
from functools import reduce
def mean(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers)