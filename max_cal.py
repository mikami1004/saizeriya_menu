import pandas as pd

# CSV読み込み
df = pd.read_csv("saizeriya_menu.csv")

# データの成型
df = df.dropna(subset=["税込価格(円)", "カロリー(kcal)"]) # NaNを消去(念のため)
df["税込価格(円)"] = df["税込価格(円)"].astype(int)
df["カロリー(kcal)"] = df["カロリー(kcal)"].astype(int)

# ナップサック：制限1000円
budget = 1000
n = len(df)

# dp[i][w] : i番目までの商品から選んで合計w円以下で得られる最大カロリー
dp = [[0]*(budget+1) for _ in range(n+1)]

# DPテーブルを埋める
for i in range(n):
    cost = df.iloc[i]["税込価格(円)"]
    cal = df.iloc[i]["カロリー(kcal)"]
    for w in range(budget+1):
        if w >= cost:
            dp[i+1][w] = max(dp[i][w], dp[i][w-cost] + cal)
        else:
            dp[i+1][w] = dp[i][w]

# 最適解の復元
w = budget
chosen_items = []
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        item = df.iloc[i-1]
        chosen_items.append(item)
        w -= item["税込価格(円)"]

# 結果表示
total_price = sum(item["税込価格(円)"] for item in chosen_items)
total_cal = sum(item["カロリー(kcal)"] for item in chosen_items)

print("=== 1000円以内で最大カロリーを得られる組み合わせ（重複なし） ===")
for item in reversed(chosen_items):
    print(f"- {item['商品名']} | {item['税込価格(円)']}円 | {item['カロリー(kcal)']}kcal")
print(f"\n▶ 合計: {total_price}円, {total_cal}kcal")
