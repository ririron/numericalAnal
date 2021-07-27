###############################################################################
# クラス定義
class MyVec2:
    # クラス属性
    a = 1     # 通常の属性
    _a = 10   # 安易に変更してほしくない属性は変数名を _ で始める
    __a = 100 # 属性を隠蔽したい場合は変数名を __ で始める

    # オブジェクト作成時に呼び出される関数
    def __init__(self, x, y):
        """
        ２次元座標 (x, y) を渡し、ベクトルとして保持する。
        """
        self.x = x
        self.y = y

    # MyVec2 クラスが持つメソッドの定義
    def area(self):
        """
        原点と (self.x, self.y) を対角点とする長方形の面積を戻す。
        """
        return abs(self.x) * abs(self.y)

    def dot(self, u):
        """
        MyVec2 オブジェクト同士の内積を戻す。
        """
        return self.x*u.x + self.y*u.y

###############################################################################
# MyVec2 オブジェクトを作成
v = MyVec2(2, 2) # この引数は __init__ メソッドに渡される
print("type of v:", type(v))

# オブジェクトが持つメンバ(属性およびメソッド)には . で区切ってアクセスする
print("v.x = ", v.x, ", v.y = ", v.y)
print("v.a = ", v.a, ", v._a = ", v._a)
#print("v.__a = ", v.__a) # __a 属性は隠蔽されており、(この名前では)外部からアクセス不可能

print("area of v = ", v.area())
u = MyVec2(0,1)
print("dot: ", v.dot(u))

# オブジェクトに新しい属性を追加するには、新しい変数に直接代入
v.str = "added attribute"
print("v.str = ", v.str)

# オブジェクトのメンバ一覧
print("Attributes and methods of v:\n", dir(v))



###############################################################################
# クラスの継承
class MyVec3(MyVec2): # スーパークラスを渡す。スーパークラスは複数渡す事もできる。
    # スーパークラスと同じ名前の属性・メソッドは上書きされる
    def __init__(self, x, y, z):
        """
        3次元座標 (x, y, z) を渡し、ベクトルとして保持する。
        """
        # 推奨されない記述
        #self.x = x
        #self.y = y
        #self.z = z
        # スーパークラスのメソッドを呼び出す時は super() を使う
        super().__init__(x, y)
        self.z = z

    # MyVec3 クラスが持つメソッドの定義
    def volume(self):
        """
        原点と (self.x, self.y, self.z) を対角点とする直方体の体積を戻す。
        """
        return abs(self.x) * abs(self.y) * abs(self.z)

    def dot(self, u):
        """
        MyVec3 オブジェクト同士の内積を戻す。
        """
        return self.x*u.x + self.y*u.y + self.z*u.z

    def __add__(self, u):
        """
        MyVec3 オブジェクト同士の和を戻す(加算 + の定義)。
        """
        return MyVec3(self.x + u.x, self.y + u.y, self.z + u.z)

    def __iadd__(self, u):
        """
        MyVec3 オブジェクト同士の和を戻す(複合演算子 += の定義)。
        """
        self.x += u.x
        self.y += u.y
        self.z += u.z
        return self

    def __str__(self):
        """
        MyVec3 オブジェクトを文字列型への変換(print 関数で暗黙に呼び出される)。
        """
        return "[{0}, {1}, {2}]".format(self.x, self.y, self.z)

###############################################################################
# MyVec3 オブジェクトを作成
v = MyVec3(3, 3, 3)
print("\ntype of v:", type(v))

# MyVec3 オブジェクトはスーパークラスである MyVec2 クラスの属性・メソッドを引き継ぐ
print("v.a = ", v.a, ", v._a = ", v._a)
print("v.x = ", v.x, ", v.y = ", v.y, ", v.z = ", v.z)
print("area of v = ", v.area())

# MyVec3 クラスで新規定義、上書き定義されたメソッド
print("volume of v = ", v.volume())
print("dot: ", v.dot(MyVec3(0,1,2)))

u = v + MyVec3(0,1,2) # __add__ メソッドが呼び出される
print("u.x = ", u.x, ", v.y = ", u.y, ", v.z = ", u.z)
v += MyVec3(0,1,2) # __iadd__ メソッドが呼び出される
print("v = ", v)   # __str__ メソッドが呼び出される



class MyPolynomial:
    def __init__(self, a, b, c):
        """
        2次多項式 a*x**2 + b*x + c の係数を渡す．
        """
        print("オブジェクトを作成した際に呼び出されるメソッドです")

    def value(self, x):
        """
        2次多項式 a*x**2 + b*x + c の値を戻す．
        """
        return print("2次多項式の値を戻したい！")

    def root(self):
        """
        2次方程式 a*x**2 + b*x + c = 0 の解 x のリストを戻す．
        """
        return print("2次方程式の解のリストを戻したい！")

p = MyPolynomial(2, 1, 1)
print("polynomial value:", p.value(2))
print("polynomial root:", p.root())










