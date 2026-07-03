import pandas as pd

# レビュー読み込み
df = pd.read_csv("data/raw/sample_reviews.csv")

# カテゴリ分類
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

# カテゴリ追加
df["category"] = df["review"].apply(classify)

# 件数集計
summary = df["category"].value_counts()

# Blueprint作成
output = "# Enablement Blueprint\n\n"

for category, count in summary.items():

    output += f"## {category}\n\n"
    output += f"レビュー件数：{count}件\n\n"

    if category == "待ち時間":
        output += """原因候補
- 人員不足
- ピーク時間の混雑
- 受付フロー

改善案
- シフト最適化
- 受付導線改善
- セルフ受付導入

"""

    elif category == "店員対応":
        output += """原因候補
- 説明品質のばらつき
- 教育不足

改善案
- ロールプレイング
- FAQ更新
- トークスクリプト改善

"""

    output += "---\n\n"

# Markdown保存
with open("docs/enablement_blueprint.md", "w", encoding="utf-8") as f:
    f.write(output)

print("Blueprintを生成しました！")