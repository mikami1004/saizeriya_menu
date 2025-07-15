import pandas as pd

# CSV読み込み
df = pd.read_csv("saizeriya_menu.csv")

# データの成型
df = df.dropna(subset=["税込価格(円)", "カロリー(kcal)"])
df["税込価格(円)"] = df["税込価格(円)"].astype(int)
df["カロリー(kcal)"] = df["カロリー(kcal)"].astype(int)

budget = 1000
n = len(df)

# dp[w]: 価格w円以下で得られる最大カロリー
dp = [0] * (budget + 1)

# 最適解の復元用の配列（どの商品を最後に選んだかのインデックス）
choice = [-1] * (budget + 1)

for w in range(budget + 1):
    for i in range(n):
        cost = df.iloc[i]["税込価格(円)"]
        cal = df.iloc[i]["カロリー(kcal)"]
        if cost <= w:
            val = dp[w - cost] + cal
            if val > dp[w]:
                dp[w] = val
                choice[w] = i

# 最適な組み合わせの復元
w = budget
chosen_items = []
while w > 0 and choice[w] != -1:
    i = choice[w]
    item = df.iloc[i]
    chosen_items.append(item)
    w -= item["税込価格(円)"]

# 集計と表示
total_price = sum(item["税込価格(円)"] for item in chosen_items)
total_cal = sum(item["カロリー(kcal)"] for item in chosen_items)

print("=== 1000円以内で最大カロリーを得る組み合わせ（重複あり） ===")
for item in chosen_items:
    print(f"- {item['商品名']} | {item['税込価格(円)']}円 | {item['カロリー(kcal)']}kcal")
print(f"\n▶ 合計: {total_price}円, {total_cal}kcal")
