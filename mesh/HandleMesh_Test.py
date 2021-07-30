import HandleMesh
import numpy as np
import pprint

def saddle_func(x, y):
    return (x-0.5)**2 - (y-0.5)**2

def func(x):
    return 2 * np.pi**2 * np.sin(np.pi * x[:, 0]) + np.sin(np.pi * x[:, 1])


tobj = HandleMesh.HandleMesh("R5")
val = saddle_func(tobj.n2c[:,0], tobj.n2c[:,1])


p2p = tobj.getPoint2Point()
L = np.zeros([20, 20])
D = np.zeros([20, 20])

for i, e in enumerate(tobj.e2n):

    fm  = tobj.getFmArray(p2p[i])
    ri  = tobj.getRiArray(p2p[i])
    for y in range(3):
        for x in range(3):
            L[e[x]-1, e[y]-1] += fm[y, x]
            D[e[x]-1, e[y]-1] += ri[y, x]

#今，上底の5接点にディレクレ境界条件が課されているので，
#15~19の行を変更
D[15:, :] = np.eye(20)[15:, :]

D[0:5, :] = np.eye(20)[0:5, :]

# 右辺ベクトルの作成
b = np.zeros(20, dtype=np.float64)
for k in range(len(tobj.e2n)):
    node = tobj.e2n[k] - 1
    p = tobj.n2c[node]
    b[node] += tobj.getFmArray(p).dot(func(p))


uh = np.linalg.solve(D, b)
print(uh)
tobj.show3dMeshData(uh)