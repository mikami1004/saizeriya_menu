import requests
import pandas as pd

url = "https://allergy.saizeriya.co.jp/view?lg=ja"
resp = requests.get(url)
data = resp.json()["body"]

grand_menu = [item for item in data if item.get("category") == "グランド"]

# データ整形
df = pd.DataFrame(grand_menu)
df = df[["name", "includigTaxPrice", "calorie"]]
df.columns = ["商品名", "税込価格(円)", "カロリー(kcal)"]

# 保存
df.to_csv("saizeriya_menu.csv", index=False)
print(df.head())