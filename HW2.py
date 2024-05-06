import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b' 
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "The total income of the employee consists of several parts: $1999.01 as the main income,\
      supplemented by additional receipts of $26.99 and $324.00."
total_income = sum_profit(text, generator_numbers)
print(f"The total income: {total_income} dollars")


