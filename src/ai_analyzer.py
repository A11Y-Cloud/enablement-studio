import pandas as pd

df = pd.read_csv("data/raw/sample_reviews.csv")

print(df["review"])