import pandas as pd

# CSVを読み込む
df = pd.read_csv("data/raw/sample_reviews.csv")

# 件数表示
print(f"レビュー件数：{len(df)}件")

print("\n========== データ ==========\n")

print(df)