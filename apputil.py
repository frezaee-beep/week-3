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

# Exercise 3

def load_bellevue():
    url = "https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv"
    return pd.read_csv(url)


def task_1():
    df_bellevue = load_bellevue()

    # Treat invalid gender values as missing
    df_bellevue.loc[
        ~df_bellevue["gender"].isin(["m", "w"]),
        "gender"
    ] = pd.NA

    missing_counts = df_bellevue.isna().sum()
    sorted_columns = missing_counts.sort_values().index.tolist()

    return sorted_columns


def task_2():
    df_bellevue = load_bellevue()

    df_bellevue["year"] = pd.to_datetime(
        df_bellevue["date_in"]
    ).dt.year

    admissions = (
        df_bellevue
        .groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )

    return admissions


def task_3():
    df_bellevue = load_bellevue()

    # Treat invalid gender values as missing
    df_bellevue.loc[
        ~df_bellevue["gender"].isin(["m", "w"]),
        "gender"
    ] = pd.NA

    average_age = (
        df_bellevue
        .groupby("gender")["age"]
        .mean()
    )

    return average_age


def task_4():
    df_bellevue = load_bellevue()

    professions = (
        df_bellevue["profession"]
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    return professions
