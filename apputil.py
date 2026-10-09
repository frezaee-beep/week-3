import seaborn as sns
import pandas as pd
from functools import reduce


# update/add code below ...
#Excercise 1: Write a function that takes an integer n as input and returns the nth Fibonacci number. The Fibonacci sequence is defined as follows: 

def fibonacci(n):
    """Return the nth number in the Fibonacci sequence."""
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

 # Exercise 2: Convert an integer to its binary representation using recursion.
def to_binary(n):
    """Return the binary representation of an integer as a string."""
    if n < 2:
        return str(n)

    return to_binary(n // 2) + str(n % 2)
# Excercise 3:

def matching_brackets(sequence):
    """Return True when all brackets in the sequence are correctly matched."""
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



# Excercise 4: 

def mean(numbers):
    """Return the arithmetic mean of a sequence of numbers."""
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers)

# Exercise 3

def load_bellevue():
    """Load and return the Bellevue Almshouse dataset as a DataFrame."""
    url = "https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv"
    return pd.read_csv(url)



def task_1():
    """Return column names ordered from least to most missing values."""
    df_bellevue = load_bellevue()

    # Treat invalid gender values as missing.
    df_bellevue.loc[
        ~df_bellevue["gender"].isin(["m", "w"]),
        "gender"
    ] = pd.NA

    missing_counts = df_bellevue.isna().sum()
    sorted_columns = missing_counts.sort_values().index.tolist()

    return sorted_columns


def task_2():
    """Return total Bellevue admissions for each year as a DataFrame."""
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
    """Return the average age for each gender as a pandas Series."""
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
    """Return a list of the five most common professions."""
    df_bellevue = load_bellevue()

    professions = (
        df_bellevue["profession"]
        .value_counts()
        .head(5)
        .index
        .tolist()
    )

    return professions
