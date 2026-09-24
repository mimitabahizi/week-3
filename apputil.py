import seaborn as sns
import pandas as pd

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)



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
    
def task_1():
    df = df_bellevue.copy()

    # The gender column contains invalid values: ?, g, and h.
    invalid_gender = ~df["gender"].isin(["m", "w"])

    if invalid_gender.any():
        print("Invalid gender values were converted to missing values.")
        df.loc[invalid_gender, "gender"] = pd.NA

    return df.isna().sum().sort_values().index.tolist()


def task_2():
    df = df_bellevue.copy()

    df["year"] = pd.to_datetime(df["date_in"]).dt.year

    return (
        df.groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )


def task_3():
    df = df_bellevue.copy()

    # The gender column contains invalid values: ?, g, and h.
    invalid_gender = ~df["gender"].isin(["m", "w"])

    if invalid_gender.any():
        print("Invalid gender values were converted to missing values.")
        df.loc[invalid_gender, "gender"] = pd.NA

    return df.groupby("gender")["age"].mean()


def task_4():
    return df_bellevue["profession"].value_counts().head(5).index.tolist()