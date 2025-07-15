# このリポジトリについて
サイゼリヤのメニューの1000円で最大カロリーを得る組み合わせを動的計画法で解くためのコード（ファイル）たちです。

# 各ファイルの説明
- [get_menu.py](https://github.com/mikami1004/saizeriya_menu/blob/main/get_menu.py)<br>
  サイゼリヤのカロリー情報サイト([これ](https://allergy.saizeriya.co.jp/allergy))からスクレイピングするプログラム。saizeriya_menu.csvの情報が古くなってきたらこのコードを使ってください。
- [max_cal.py](https://github.com/mikami1004/saizeriya_menu/blob/main/max_cal.py)<br>
  重複なしの組み合わせを求めるコード
- [max_cal2.py](https://github.com/mikami1004/saizeriya_menu/blob/main/max_cal2.py)<br>
  重複ありの組み合わせを求めるコード
- [saizeriya_menu.csv](https://github.com/mikami1004/saizeriya_menu/blob/main/saizeriya_menu.csv)<br>
  2025/07/15時点でのメニューデータ
