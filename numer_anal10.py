import numpy
import matplotlib
import matplotlib.pyplot
import mpl_toolkits.mplot3d
import matplotlib.animation

plotall = True  # 全てのサンプルコードを実行する
#plotall = False # 全てのサンプルコードを実行しない

# 日本語フォントを指定する
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Helvetica', 'Takao', 'IPAexGothic', 'IPAPGothic', 'Meirio']
# 上でダメだったら次のように指定する事もできる
jpf = matplotlib.font_manager.FontProperties(fname=r"/Users/takanotaigo/Library/Fonts/TakaoPGothic.ttf")
#jpf = matplotlib.font_manager.FontProperties(fname=r"C:\Windows\Fonts\meiryo.ttc")
#matplotlib.rcParams['font.family'] = jpf.get_name()
# pdflatex で数式を作成 ***日本語フォントと併用しようとするとエラーになる***
#matplotlib.rcParams["text.usetex"] = True

x = numpy.linspace(0,2*numpy.pi,101) # [0,2*pi] の 101 個の等分割点を作成

#%% 簡単なグラフの描画
#if True:
if plotall:
    y = numpy.sin(x)            # x の成分ごとの sin(x) を計算
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    matplotlib.pyplot.plot(x,y) # 点 (x[i],y[i]) を繋いだグラフを描画
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% 複数のグラフの描画
#if True:
if plotall:
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    matplotlib.pyplot.plot(x, numpy.sin(x), x, numpy.cos(x))
    #matplotlib.pyplot.plot([0,6], [0.5,0.5]) # show する前なら plot を使って追記できる
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% オプションの指定
#if True:
if plotall:
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    linestyles = ['-', '--', ':']
    markers = ['D', 's', 'H', '|', '^', '_', 'd', ',', 'x', '.', 'o', 'h', \
               '*', '+', '4', 'v', 'p', '1', '2', '3', '<', '>', '8', '_']
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    matplotlib.pyplot.plot(x, numpy.sin(x), "ro", \
        x, numpy.cos(x), linestyles[2]+markers[0]+colors[0])
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% タイトル、軸、凡例の指定
#if True:
if plotall:
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    # パラメータ曲線も描画できる
    matplotlib.pyplot.plot(numpy.cos(x), numpy.sin(x), color="#11cc55") # color は RGB hex で指定できる
    matplotlib.pyplot.xlim(-1.5, 1.5) # x 軸の描画範囲
    matplotlib.pyplot.ylim(-1.5, 1.5) # y 軸の描画範囲
    matplotlib.pyplot.title("circle") # タイトルをつける
    matplotlib.pyplot.xlabel("x-label") # x 軸に名前をつける
    matplotlib.pyplot.ylabel("y-label") # y 軸に名前をつける
    matplotlib.pyplot.legend(["curve"], loc=2) # 凡例をつける
    #matplotlib.pyplot.savefig("fig_plot.jpg", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% axes オブジェクトを利用した描画
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots()  # figure と axes オブジェクトを作成
    ax.plot(numpy.cos(x), numpy.sin(x), lw=2) # lw は線の太さ
    ax.set_aspect("equal")       # 縦横比を 1:1 にする
    ax.set_xlim(-1.2, 1.2)       # axes メソッドとして x 軸の描画範囲を変更する
    ax.set_xlabel(r"$x$", fontsize=20)             # TeX の数式を利用できる
    ax.set_ylim(-1.2, 1.2)
    ax.set_ylabel(r"$y$", fontsize=20, rotation=0) # rotation で傾きを変更できる
    ax.set_title("circle", family="serif", fontsize=40) # フォントやサイズも変更できる
    #matplotlib.pyplot.savefig("fig_plot.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% matplotlib.pyplot 関数と axes メソッドの関係
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots(3)  # figure と axes オブジェクトを作成
    ax[0].plot(x, numpy.cos(x))  # ax.plot メソッドは指定した axes オブジェクトに描画
    matplotlib.pyplot.plot(x, numpy.sin(x)) # plot 関数は ax[-1] に描画
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% 対数グラフ
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots()  # figure と axes オブジェクトを作成
    ax.plot(x, numpy.exp(x), label=r"$e^x$") # ax に描画
    #ax.set_xscale("log")         # x 軸を log スケールにする
    ax.set_yscale("log")         # y 軸を log スケールにする
    ax.legend(loc=2)             # 凡例を書く場所を指定
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% エラーバーの描画
#if True:
if plotall:
    t = numpy.linspace(0,2*numpy.pi,11)
    y = numpy.sin(t)            # x の成分ごとの sin(x) を計算
    err = numpy.cos(t) / 3    # 適当に誤差の幅を作る
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    matplotlib.pyplot.errorbar(t, y, err)
    #matplotlib.pyplot.savefig("fig_errorbar.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% グラフの間も描画
#if True:
if plotall:
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    y = numpy.sin(x)
    matplotlib.pyplot.fill_between(x, y, color="gray", alpha=0.5) # グラフと x 軸までを透過描画
    y = numpy.cos(x)
    matplotlib.pyplot.fill_between(x, 0.8*y, 1.2*y, color="blue", alpha=0.5) # 2本のグラフの間を透過描画
    #matplotlib.pyplot.savefig("fig_fill_between.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% 散布図の描画
#if True:
if plotall:
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    area = 200*numpy.random.rand(len(x))**2 # 散布図の点の大きさ
    colors = numpy.random.rand(len(x))  # 点の色
    matplotlib.pyplot.scatter(x, numpy.sin(x), s=area, c=colors, alpha=0.5)
    #matplotlib.pyplot.savefig("fig_scatter.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% 棒グラフの描画
#if True:
if plotall:
    t = numpy.arange(10)
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    matplotlib.pyplot.bar(t, numpy.cos(t), facecolor="cyan", edgecolor="white")
    #matplotlib.pyplot.savefig("fig_bar.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% ヒストグラムの描画
#if True:
if plotall:
    t=numpy.random.randn(100000)
    fig, ax = matplotlib.pyplot.subplots()  # figure と axes オブジェクトを作成
    ax.hist(t, density=True)     # ヒストグラムを描画，density は確率密度関数にする
    ax.set_title("ヒストグラム", fontsize=14, fontproperties=jpf)
    ax.set_xlim((min(t),max(t)))
    #matplotlib.pyplot.savefig("fig_hist.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる
    
    fig, ax = matplotlib.pyplot.subplots()  # figure と axes オブジェクトを作成
    ax.hist(t, cumulative=True, bins=50) # cumulative は累積表示，bins は棒の数
    ax.set_title("累積ヒストグラム", fontsize=14, fontproperties=jpf)
    ax.set_xlim((min(t),max(t)))
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% 3D 曲線の描画
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots(subplot_kw={"projection":"3d"}) # 3D グラフと宣言
    ax.plot(numpy.cos(3*x), numpy.sin(3*x), 3*x, "-b")
    #matplotlib.pyplot.savefig("fig_plot3d.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% 3D グラフの描画
x = numpy.linspace(0, 2*numpy.pi, 21)       # x 軸 [0,2*pi] を 20 等分割
y = numpy.linspace(-numpy.pi, numpy.pi, 31) # y 軸 [-pi,pi] を 30 等分割
X, Y = numpy.meshgrid(x, y)                 # xy 平面上の格子点を作成
Z = numpy.sin(X)+ numpy.cos(Y)              # 格子点上の関数値を全て計算
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots(subplot_kw={"projection":"3d"}) # 3D グラフと宣言
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="hot",  linewidth=0) # 曲面の描画
    #ax.plot_wireframe(X, Y, Z)            # ワイヤーフレーム描画
    #ax.contour3D(X, Y, Z)                 # 等高線の描画
    #ax.contourf3D(X, Y, Z)                # 等高線の間を塗りつぶす
    #ax.scatter3D(numpy.ravel(X), numpy.ravel(Y), numpy.ravel(Z)) # 散布図
    #ax.view_init(elev=20, azim=140)       # 視点の角度を指定する
    #matplotlib.pyplot.savefig("fig_3d.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% 特定の図形の描画
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots(subplot_kw={"projection":"3d"})
    linpts = list() # 3次元空間での折れ線の頂点のリストを作る
    linpts.append([(0,0,0), (1,1,0), (1,1,1)]) # 折れ線の点 (x_i,y_i,z_i) を追加
    linpts.append([(0,0,1), (0,1,0)]) # 2本目の折れ線の点
    linart = mpl_toolkits.mplot3d.art3d.Line3DCollection(linpts, color="red")
    ax.add_collection3d(linart)
    tripts = list() # 3次元空間での三角形の頂点のリストを作る
    tripts.append([(0,0,0), (1,0,0), (0,1,0)]) # (x_i,y_i,z_i) を頂点とする三角形を追加
    tripts.append([(0,1,1), (1,0,0), (1,1,1)])
    triart = mpl_toolkits.mplot3d.art3d.Poly3DCollection(tripts, alpha=.25, edgecolor="black")
    ax.add_collection3d(triart)
    ax.set_aspect("auto") # 縦横比を 1:1 にする
    ax.set_xlabel(r"$x$", fontsize=20)
    ax.set_ylabel(r"$y$", fontsize=20)
    ax.set_zlabel(r"$z$", fontsize=20)
    #matplotlib.pyplot.savefig(fig_tri.pdf, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% 等高線図の描画
#if True:
if plotall:
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    matplotlib.pyplot.contourf(X, Y, Z, 10, alpha=0.75) # 10 本の等高線図
    C = matplotlib.pyplot.contour(X, Y, Z, 10, colors="black", linewidths=0.5)
    matplotlib.pyplot.clabel(C, inline=1, fontsize=10)
    #matplotlib.pyplot.savefig("fig_contourf.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% 濃淡図の描画
#if True:
if plotall:
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    matplotlib.pyplot.imshow(Z, interpolation="none", cmap="gray")
    #matplotlib.pyplot.imshow(Z, interpolation="nearest", cmap="bone", origin="lower")
    #matplotlib.pyplot.savefig("fig_imshow.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% ベクトル場の描画
#if True:
if plotall:
    matplotlib.pyplot.figure()  # 描画ウィンドウを作成
    matplotlib.pyplot.contour(X, Y, Z, 10)
    matplotlib.pyplot.quiver(X, Y, numpy.cos(X), -numpy.sin(Y), pivot="middle", color="gray")
    #matplotlib.pyplot.savefig("fig_quiver.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% 複数のグラフの描画
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots(1,3,figsize=(12,4)) # 1行3列の描画領域を確保
    ax[0].plot(x, 8*x, x, x**2)
    ax[0].set_title("default range") # デフォルトの描画範囲はグラフが収まる範囲を描画
    ax[1].plot(x, 8*x, x, x**2)
    ax[1].axis("tight")              # tight range はグラフが存在する範囲を描画
    ax[1].set_title("tight range")
    ax[2].plot(x, 8*x, x, x**2)
    ax[2].set_xlim([0,5])            # x 軸の描画範囲を指定
    ax[2].set_ylim([0,40])           # y 軸の描画範囲を指定
    ax[2].set_title("custom range")
    #matplotlib.pyplot.savefig("fig_subplots.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% グリッドの描画
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots(2,2,figsize=(8,8)) # 2行2列の描画領域を確保
    fig.suptitle("Figure title")
    ax[0][0].plot(x, 8*x, x, x**2)
    ax[0][0].grid(True)
    ax[0][0].set_title("default grid")
    ax[0][1].set_title("axes01 title")
    ax[1][0].set_title("axes10 title")
    ax[1][1].plot(x, 8*x, x, x**2)
    ax[1][1].grid(color="r", alpha=0.5, linestyle="dashed", linewidth=0.5)
    ax[1][1].set_title("custom grid")
    #matplotlib.pyplot.savefig("fig_grid.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% 二重軸
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(x, 8*x, color="blue")
    ax.set_ylabel(r"$y = 8x$", fontsize=20, color="blue")
    for label in ax.get_yticklabels(): # 左側の軸の色を全て青にする
        label.set_color("blue")
    tx = ax.twinx()                    # 右側の軸を追加
    tx.plot(x, x**3, color="red")
    tx.set_ylabel(r"$y = x^3$", fontsize=20, color="red")
    for label in tx.get_yticklabels(): # 左側の軸の色を全て青にする
        label.set_color("red")
    #matplotlib.pyplot.savefig("fig_twinx.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% 軸の場所の変更
#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots(3,1,figsize=(12,8)) # 3行1列の描画領域を確保
    t = numpy.linspace(-numpy.pi, numpy.pi, 21)
    ax[0].plot(t, numpy.sin(t))
    ax[0].xaxis.tick_top()                      # x 軸を上に描画する
    ax[0].yaxis.tick_right()                    # y 軸を右に描画する
    ax[1].plot(t, numpy.cos(t))
    ax[1].spines["left"].set_position("zero")   # 左の軸を x=0 の位置に書く
    ax[1].spines["right"].set_color("none")     # 右の軸を描画しない
    ax[1].spines["bottom"].set_position("zero") # 下の軸を y=0 の位置に書く
    ax[1].spines["top"].set_color("none")       # 上の軸を描画しない
    ax[1].xaxis.set_ticks_position("bottom")    # 下の軸に目盛りを書く
    ax[1].yaxis.set_ticks_position("left")      # 左の軸に目盛りを書く
    ax[1].set_xticks([-numpy.pi, -0.5*numpy.pi, 0.0,
                      0.5*numpy.pi, numpy.pi])  # x 軸の刻み位置
    ax[1].set_xticklabels(["$-\pi$", "$-\pi/2$", 0,
                      "$\pi/2$", "$\pi$"])      # x 軸の刻み位置に表示する文字(TeX命令も可能)
    ax[1].set_yticks([-1.0, -0.5, 0.5, 1.0])    # y 軸の刻み位置
    ax[1].set_yticklabels(["-1", "-0.5", "0.5", "1"]) # y 軸の刻み位置に表示する文字
    ax[2].plot(t, numpy.sin(2*t))
    ax[2].spines["left"].set_color("none")      # 左の軸を描画しない
    ax[2].spines["right"].set_color("none")     # 右の軸を描画しない
    ax[2].spines["bottom"].set_color("none")    # 下の軸を描画しない
    ax[2].spines["top"].set_color("none")       # 上の軸を描画しない
    ax[2].set_xticks([])                        # x 軸，目盛りを描画しない
    ax[2].set_yticks([])                        # y 軸，目盛りを描画しない
    #matplotlib.pyplot.savefig("fig_spines.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% 軸の共有
#if True:
if plotall:
    t = numpy.linspace(0, 10*numpy.pi, 401)
    fig, ax = matplotlib.pyplot.subplots(3,1,figsize=(12,8), sharex=True, sharey=True)
    fig.subplots_adjust(hspace=0) # 各グラフのマージンを0にする
    ax[0].plot(t, numpy.sin(t))
    ax[1].plot(t, numpy.sin(2*t))
    ax[2].plot(t, numpy.sin(4*t))
    ax[0].set_xlim([0,2*numpy.pi])
    #matplotlib.pyplot.savefig("fig_share.png", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% 図中に文字を描画
#if True:
if plotall:
    x = numpy.linspace(-numpy.pi, numpy.pi, 201)
    fig, ax = matplotlib.pyplot.subplots()
    ax.plot(x, numpy.cos(x))
    ax.grid(True)
    # 文字の描画
    ax.text(0.0, 1.0, "最大値", size=10, fontproperties=jpf)
    ax.text(0.0, 0.0, "原点", size=15, fontproperties=jpf, 
            horizontalalignment=["left", "center", "right"][1],
            verticalalignment=["bottom", "center", "top"][1])
    ax.text(1.1, 0.5, r"$\cos\theta$", size=15, color="red", rotation=45)
    # 囲み文字の描画
    boxdic = {"facecolor":"lightblue", "edgecolor":"gray",
              "boxstyle":"Round", "linewidth":2}
    ax.text(-2.0, -0.75, "Python", size=15, bbox=boxdic)
    # matplotlib.pyplot.text 関数でも文字を描画できる
    matplotlib.pyplot.text(1.5, -1.0, "minimum", size=15, alpha=0.5, backgroundcolor="lightgreen")
    #matplotlib.pyplot.savefig("fig_text.jpg", dpi=300, bbox_inches="tight")
    matplotlib.pyplot.show()    # 実際にグラフを描画する
    #matplotlib.pyplot.close()   # 描画ウィンドウを閉じる

#%% アニメーション
#   アニメーションする画像を予めすべて描画する場合
#if True:
if plotall:
    # matplotlib.pyplot.***() 関数を使う場合
    if 1:
        fig = matplotlib.pyplot.figure()
        artists = []
        for n in range(100):
            t = numpy.arange(0, n*0.1, 0.1)
            x = numpy.cos(t)/(1+0.05*t)
            y = numpy.sin(t)/(1+0.05*t)
            artists.append(matplotlib.pyplot.plot(x, y, "b"))
    # axes メソッドを使う場合
    else:
        fig, ax = matplotlib.pyplot.subplots()
        artists = []
        for n in range(100):
            t = numpy.arange(0, n*0.1, 0.1)
            x = numpy.cos(t)/(1+0.05*t)
            y = numpy.sin(t)/(1+0.05*t)
            frame = ax.plot(x, y, "b") # 戻り値はリスト型
            frame.append(ax.annotate("Frame:{0:0>4}".format(n), (-0.8,-0.8)))
            artists.append(frame)
    # NOTE: タイトルを付けたアニメーションを作る事ができなかった

    ani = matplotlib.animation.ArtistAnimation(fig, artists, interval=50, blit=True)
    #ani.save("fig_animation.mp4", writer="ffmpeg", fps=30, bitrate=1800)
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% アニメーションする画像をその都度描画する場合
def plot_spiral(n, step=0.1, axes=None):
    """
    第 n フレームでの曲線を描画する関数．
    第1引数はフレーム番号を渡す変数にしなければならない．
    第2引数以降の変数には fargs で渡されたリストが代入される．
    """
    # matplotlib.pyplot.***() 関数を使う場合
    if axes == None:
        matplotlib.pyplot.clf()           # figure オブジェクトに描画されているグラフを消去
        t = numpy.arange(0, n*step, step)
        x = numpy.cos(t)/(1+0.05*t)
        y = numpy.sin(t)/(1+0.05*t)
        matplotlib.pyplot.plot(x, y)      # 曲線を描画
        matplotlib.pyplot.title("Step:{1}, Frame:{0:0>4}".format(n,step))
        matplotlib.pyplot.xlim(-1.2, 1.2) # x 軸の描画範囲
        matplotlib.pyplot.ylim(-1.2, 1.2) # y 軸の描画範囲
    # axes メソッドを使う場合
    else:
        ax.cla()                          # axes オブジェクトに描画されているグラフを消去
        t = numpy.arange(0, n*step, step)
        x = numpy.cos(t)/(1+0.05*t)
        y = numpy.sin(t)/(1+0.05*t)
        ax.plot(x, y)                     # 曲線を描画
        ax.set_title("Axes:Given, Step:{1}, Frame:{0:0>4}".format(n,step))
        ax.set_xlim(-1.2, 1.2)            # x 軸の描画範囲
        ax.set_ylim(-1.2, 1.2)            # y 軸の描画範囲

#if True:
if plotall:
    fig, ax = matplotlib.pyplot.subplots()
    ani = matplotlib.animation.FuncAnimation(fig, plot_spiral, interval=50, frames=100,
                                             fargs=[0.5]) # plot_spiral に ax を渡さない場合
                                             #fargs=[0.5,ax]) # plot_spiral に ax を渡す場合
    #ani.save("fig_animation.mp4", writer="ffmpeg", fps=30, bitrate=1800)
    matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる

#%% 練習問題
#if True:
if plotall:
    # 要素・節点対応表と節点・座標対応表を作成
    e2n = numpy.array([[1,2,7], [2,3,8], [1,7,6]]) - 1
    n2c = numpy.array([[0.0,0.0], [0.25,0.0], [0.5,0.0], [0.75,0.0], [1.0,0.0],
                       [0.0,1/3], [0.25,1/3], [0.5,1/3], [0.75,1/3], [1.0,1/3]])
    print("e2n = ")
    print(e2n)
    print("\nn2c = ")
    print(n2c)
    # figure, axes オブジェクトを用意
    fig, ax = matplotlib.pyplot.subplots()
    for k in range(len(e2n)):
        node = e2n[k] # 第 k 要素の節点番号を取得
        p = n2c[node] # 節点番号に対応する座標を取得
        print("\n頂点の座標が\n", p, "\nとなる三角形を(一枚の絵に)描画してください．")
    #matplotlib.pyplot.savefig("tri.pdf", bbox_inches="tight")
    #matplotlib.pyplot.show()     # 実際にグラフを描画する
    #matplotlib.pyplot.close(fig) # 描画ウィンドウを閉じる










