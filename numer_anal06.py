print("\n分岐・反復処理")
n = 5
m = 9
if 1 <= n < m:
    print(n, "は1以上かつ", m, "未満です。")
else:
    print(n, "は1未満または", m, "以上です。")

s = "理工学"
t = "佐賀大学大学院理工学研究科"
if s is t:
    print("{0}と{1}は同じオブジェクトです。".format(s,t))

if s is not t:
    print("{0}と{1}は異なるオブジェクトです。".format(s,t))

if s in t:
    print("{0}は{1}に含まれています。".format(s,t))

for i in range(n):
    print("i = ", i)

l1 = [2, 5, 0, 1]
for j in l1:
    print("j = ", j)

l2 = ["tow", "five", "zero", "one"]
for j, k in zip(l1, l2):
    print("j = ", j, ", k = ", k)

while n > 1:
    print("n = ", n)
    n /= 2

s = {"set", -1, (1,3), 1+2j}
while s:
    x = s.pop()  # s から要素を一つ取り出して s から消去する
    print("x = ", x)

for k in l2:
    if(k == "tow"):
        continue
    print("k = ", k)
    if(k == "zero"):
        break

print("\n内包表記")
# リスト内包表記
x = [i**2 for i in range(10)]
print("x = ", x)

# 辞書内包表記
d = {i:i**2 for i in range(5)}
print("d = ", d)

# タプル内包表記はないので、リストをタプルに変換する
t = tuple([i+j for i in (10,20,30) for j in (1,2,3)])
print("t = ", t)

# 集合内包表記
n = 20
s = {i for i in range(1,n+1) if n%i == 0}
print("s = ", s)

print("\nスライス")
a = [["00","01","02","03","04"],
     ["10","11","12","13","14"],
     ["20","21","22","23","24"],
     ["30","31","32","33","34"],
     ["40","41","42","43","44"]]
print("a = ", a)
print("a[:2] = ", a[:2])
print("a[3:][1] = ", a[3:][1])
print("a[:2][:2] = ", a[:2][:2])
print("[a[i][1] for i in range(3,5)] = ", [a[i][1] for i in range(3,5)])
print("[[a[i][j] for j in range(2)] for i in range(2)] = ", [[a[i][j] for j in range(2)] for i in range(2)])
row_idx = [0,2,3]
col_idx = [2,1]
print("[[a[i][j] for j in col_idx] for i in row_idx] = ", [[a[i][j] for j in col_idx] for i in row_idx])

print("\nユーザ定義関数")
def func_name(arg):
    """
    関数の説明
    """
    return arg # 戻り値

x = func_name("test")
print("x = ", x)
help(func_name) # 関数定義直下のコメントを表示できる
#print(func_name.__doc__) # 関数定義直下のコメントを表示できる

def func_keyword(x, y):
    print("x = ", x)
    print("y = ", y)

func_keyword(1, "text")
func_keyword(y=1, x="text")

def func_default(u, v="default value"):
    print("u = ", u)
    print("v = ", v)
    return u, v

x, y = func_default(1)
print("x = ", x, ", y = ", y)
x, y = func_default("text", 10)
print("x = ", x, ", y = ", y)
x, y = func_default(v = "str", u = -1)
print("x = ", x, ", y = ", y)

print("\n変数のスコープ")
# x が定義済みであれば削除する
if x != None:
    del x
a = 10
x = -1
def func_scope():
    a = x
    print("In func_scope, a = ", a)
func_scope()
print("a = ", a)



print("\n練習問題1")
name2score = {"A":550, "B":525, "C":595, "D":545, "E":565, "F":580, \
              "G":625, "H":495, "I":660, "J":570, "K":540}
print(name2score, "を利用して練習問題を解いてみましょう．")

vals = name2score.values()



print("\n練習問題2")
def my_average(x):

    return sum(x) / len(x)

def my_median(x):
    x = sorted(x)
    if len(x) % 2 == 0:
        m = len(x) / 2
        return (x[int(m)-1] + x[int(m)]) / 2
    else :
        m = len(x) / 2 + 1
        return x[int(m)-1] 

data = [-1, 2, 10, 4]
print("my_average is ", my_average(data))
print("my_median is ", my_median(data))









