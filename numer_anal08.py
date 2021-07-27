# ファイル入出力
# 注意！このコードを実行すると幾つかのファイルを作成します！
###############################################################################
print("\nテキストファイルの書き込み/読み込み")
f = open("file_ABC.txt", "w")  # テキストファイル file_ABC.txt を作成
f.write("ABCDEFGHIJKLMN")      # 文字列を書き込む
f.close()                      # f を閉じる

f = open("file_ABC.txt", "r")    # テキストファイル読み込み専用モードでオープン
print("f.read()  = ", f.read())  # ABC.txt ファイルをすべて読み込む
print("f.seek(0) = ", f.seek(0)) # f のシーク位置をファイル先頭に戻す
print("f.read(2) = ", f.read(2)) # f から2文字読み込む．シーク位置は次の文字の場所になる
print("f.tell()  = ", f.tell())  # 現在のシーク位置の問い合わせ
print("f.seek(5) = ", f.seek(5)) # f のシーク位置をファイル先頭から数えて5文字目の所にする
print("f.read(2) = ", f.read(2)) # f から2文字読み込む．
print("f.seek(0,2) = ", f.seek(0,2)) # f のシーク位置をファイル末尾に移動させる
print("f.seek(f.tell()-3) = ", f.seek(f.tell()-3)) # 現在のシーク位置から3文字戻す
print("f.read() =  ", f.read())  # 現在のシーク位置からファイル末尾まですべて読み込む
f.close()   # f を閉じる



###############################################################################
print("\n浮動小数点数とファイル出力")
import random

a = [random.uniform(-1,1) for i in range(4)] # [-1,1) の浮動小数点数データを作成
print("a = ", a)

f = open("file_float.txt", "w") # テキストファイル file_float.txt を作成
for i in range(len(a)):
    f.write("{0:f}\n".format(a[i])) # a を文字列に変換して書き込む
f.close()                       # f を閉じる

f = open("file_float.txt", "r") # テキストファイル読み込み専用モードでオープン
ft = f.readlines()              # f をすべて読み込み，行毎の文字列のリストを作成
f.close()                       # f を閉じる
b = [float(ft[i]) for i in range(len(ft))] # ft を浮動小数点数に変換
for i in range(len(a)):
    print("a[{0}] - b[{0}] = {1:.16e}".format(i, a[i]-b[i]))

import struct

pa = struct.pack("4d", a[0], a[1], a[2], a[3]) # double 4 つをパック
print("pa = ", pa)

with open("file_float.dat", "wb") as f: # バイナリファイル file_float.dat を作成
    f.write(pa)

with open("file_float.dat", "rb") as f: # バイナリファイル file_float.dat を開く
    pb = f.read(32)                     # バイナリデータを読み込む 8*4 = 32 バイト

print("pb = ", pb)
b = struct.unpack("4d", pb)  # double 4 つにアンパック

for i in range(len(a)):
    print("a[{0}] - b[{0}] = {1:.16e}".format(i, a[i]-b[i]))



###############################################################################
print("\npickle モジュール")
import pickle

a = [1, 3.14, {"one":1, "two":2}] # pickle を使えば複雑なオブジェクトも保存できる
print("a = ", a)

with open("file_pickle.pkl", "wb") as f: # pickle で作成するファイルはバイナリファイル
    pickle.dump(a, f)                    # オブジェクトの漬物化

with open("file_pickle.pkl", "rb") as f:
    b = pickle.load(f)                   # 漬物化オブジェクトを復元

print("b = ", b)



###############################################################################
print("\nCSV ファイルの書き込み/読み込み")
import csv

a = [[11,12,13],[21,22,23],[31,32,33]]

with open("file_mat.csv", "w", encoding="utf-8", newline="") as wf:
    writer = csv.writer(wf) # csv ファイル書き込みオブジェクトを作成
    writer.writerow(["見出し0", "見出し1", "見出し2"]) # 見出しを書き込む
    for row in a:
        writer.writerow(row)

with open("file_mat.csv", "r", encoding="utf-8") as rf:
    reader = csv.reader(rf) # csv ファイル読み込みオブジェクトを作成
    header = next(reader)   # csv ファイルの最初の行(見出し)を読み込む
    print(header)
    for row in reader:
        print(row)



###############################################################################
print("\nxlsx ファイルの書き込み/読み込み")
# open 以外の関数で開いたファイルは with 文で close されない事があるので注意
import xlsxwriter

wb = xlsxwriter.Workbook("file_demo.xlsx")  # xlsx ファイルを作成
ws = wb.add_worksheet("シート名")           # ワークシートを追加
ws.write(0, 0, 100)    # セル1行1列へ整数500を書き込む
ws.write("B1", "文字") # セルの指定は文字で与えてもよい

ws_sum = wb.add_worksheet() # ワークシート名は省略できる
a = [[11,12,13],[21,22,23],[31,32,33]]
for i in range(3):
    for j in range(3):
        ws_sum.write(i, j, a[i][j])
ws_sum.write_formula(3, 0, "{=SUM(A1:A3)}") # Excel の関数も使える
ws_sum.write_formula("B4", "{=SUM(B1:B3)}") # セルの指定は文字でもよい
wb.close()



import pandas

df = pandas.read_excel("file_demo.xlsx", engine="openpyxl") # xlsx ファイルを開く
print(df)



###############################################################################
print("\nSQLite3 データベース1")
import sqlite3
conn = sqlite3.connect(":memory:") # メモリ上にデータベースを作成
cur = conn.cursor() # カーソルを作成

heading = ["ID INTEGER", "Name TEXT", "Score REAL"] # 見出しのリスト データ型は省略できる
sql = "CREATE TABLE sample ({})".format(", ".join(heading)) # 表を作る SQL 命令
print("sql = ", sql)
cur.execute(sql) # sample という表を作成

cur.execute("INSERT INTO sample VALUES (101, 'Alex', 98.1)") # sample 表に組を追加
conn.commit() # データベースに処理内容を実行する
cur.execute("SELECT * FROM sample") # sample 表のすべての組を指定する
print("cur.fetchone() = ", cur.fetchone()) # 組を１つ取り出す

lst = [[102, "Bonnie", 100.6],
       [110, "Colin", 100.0],
       [123, "Danielle", 100.7]] # sample に追加するデータのリスト
cur.executemany("INSERT INTO sample VALUES (?,?,?)", lst) # sample 表にまとめて追加
cur.execute("SELECT * FROM sample") # sample 表のすべての組を指定する
print("cur.fetchall() = ", cur.fetchall()) # 組をすべて取り出す
print("ロールバックします")
conn.rollback()
cur.execute("SELECT * FROM sample")
print("cur.fetchall() = ", cur.fetchall())

conn.close() # データベースを閉じる



###############################################################################
print("\nSQLite3 データベース2")
n_row = 3 # 表の行数
#n_row = 9999 # 表の数が多い場合
n_col = 5 # 表の列数

# 乱数データを作成
heading = ["Score{} REAL".format(j) for j in range(n_col)]

conn = sqlite3.connect("file_sqlite3.db") # データベースファイルを開く
cur = conn.cursor() # カーソルを作成
#cur.execute("PRAGMA synchronous = OFF")
#cur.execute("PRAGMA journal_mode = PERSIST")

cur.execute("SELECT * FROM sqlite_master WHERE type='table' and name='sample'")
if cur.fetchone() != None:
    print("データベースに sample 表があったので表を削除します")
    cur.execute("DROP TABLE sample")
    conn.commit()
print("データベースに sample 表を作成します")
cur.execute("CREATE TABLE sample ({})".format(", ".join(heading)))
conn.commit()

# sample に組を追加する SQL 命令
sql = "INSERT INTO sample VALUES ({})".format(",".join(["?" for _ in range(len(heading))]))
#print(sql)

if 1:
    print("1つずつ組を追加します")
    for _ in range(n_row):
        tpl = [random.random() for j in range(n_col)] # 乱数データを作成
        cur.execute(sql, tpl)          # sample 表に tpl を書き込む
        conn.commit()
else:
    print("まとめて組を追加します")
    chunk_size = 1000
    chunk = []
    for _ in range(n_row):
        tpl = [random.random() for j in range(n_col)] # 乱数データを作成
        chunk.append(tpl)               # chunk に tpl を追加 
        if len(chunk) >= chunk_size:    # chunk にあるデータ数が chunk_size 以上ならば
            cur.executemany(sql, chunk) # sample 表に chunk を書き込む
            conn.commit()
            chunk = []
    if chunk:
        cur.executemany(sql, chunk)
        conn.commit()

cur.execute("SELECT COUNT(Score0) FROM sample") # sample 表から Score0 のデータの数を求める
print("Score0 に保存されている組の数 = ", cur.fetchone())
conn.close()










