import seaborn as sns
import pandas as pd


# update/add code below ...
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def to_binary(n):
    if n < 2:
        return str(n)
    else:
        return to_binary(n // 2) + str(n % 2)