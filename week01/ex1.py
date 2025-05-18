import pandas as pd
import numpy as np

df = pd.read_csv('Housing.csv')

num = len(df)
print(f"Number of rows in dataset: {num}")

print("======================")

print(df[:6])

print("======================")

num = df.info()
emp = df.isnull().sum()

print("======================")

print(num)

print("======================")
print(emp)
