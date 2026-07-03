from pathlib import Path

master_path = Path("docs/category_master.md")

with open(master_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

categories = {}

current_category = None
reading_keywords = False

for line in lines:
    line = line.strip()

    # カテゴリ開始
    if line.startswith("## "):
        current_category = line.replace("## ", "")
        categories[current_category] = []
        reading_keywords = False

    # キーワード開始
    elif line == "キーワード":
        reading_keywords = True

    # キーワード
    elif reading_keywords and line.startswith("- "):
        keyword = line.replace("- ", "")
        categories[current_category].append(keyword)

print(categories)