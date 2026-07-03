import pandas as pd

# CSV読み込み
df = pd.read_csv("data/raw/sample_reviews.csv")


def classify(review):

    if "待ち時間" in review:
        return "待ち時間"

    elif "店員" in review or "スタッフ" in review:
        return "店員対応"

    elif "料金" in review:
        return "料金"

    elif "通信" in review:
        return "通信品質"

    elif "アプリ" in review:
        return "アプリ"

    elif "契約" in review:
        return "契約手続き"

    elif "問い合わせ" in review:
        return "問い合わせ"

    else:
        return "その他"


df["category"] = df["review"].apply(classify)

print(df[["review", "category"]])
