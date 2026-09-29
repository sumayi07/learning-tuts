# Day 25

import pandas as pd
import numpy as np

df = pd.read_csv("hacker_news.csv")
print(df.head())
print(df.tail())

title_series = df["title"]
print(title_series)

print(df.shape)

print(df[df["title"].str.contains("python", case = False)])

print(df[df["title"].str.contains("JavaScript", case = False)])