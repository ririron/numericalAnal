import HandleMesh
import numpy as np
import pprint

def saddle_func(x, y):
    return (x-0.5)**2 - (y-0.5)**2

def func(x):
    return 2 * (np.pi**2) * np.sin(np.pi * x[:, 0]) * np.sin(np.pi * x[:, 1])


tobj = HandleMesh.HandleMesh("R20")
val = saddle_func(tobj.n2c[:,0], tobj.n2c[:,1])


p2p = tobj.getPoint2Point()
<<<<<<< HEAD
print(np.shape(p2p))
L = np.zeros([20, 20])
D = np.zeros([20, 20])
=======
L = np.zeros([400, 400])
D = np.zeros([400, 400])
>>>>>>> d65e13b21c65ee1d40784977a80383ba90ca08e6

for i, e in enumerate(tobj.e2n):

    fm  = tobj.getFmArray(p2p[i])
    ri  = tobj.getRiArray(p2p[i])
    for y in range(3):
        for x in range(3):
            L[e[x]-1, e[y]-1] += fm[y, x]
            D[e[x]-1, e[y]-1] += ri[y, x]

# 右辺ベクトルの作成
b = np.zeros(400, dtype=np.float64)
for i, node in enumerate(tobj.e2n):
    p = tobj.getFmArray(p2p[i])
    b[tobj.e2n[i]-1] += p.dot(func(p2p[i]))

#ディレクレ境界条件
<<<<<<< HEAD
b[0:4]    = 0
b[15:19]  = 0
b[0:20:5] = 0
b[4:20:5] = 0

E = np.eye(np.shape(D)[0])
D[0:4, :] = E[0:4, :]
D[15:19, :] = E[15:19, :]
D[0:20:5, :] = E[0:20:5, :]
D[4:20:5, :] = E[4:20:5, :]
=======
>>>>>>> d65e13b21c65ee1d40784977a80383ba90ca08e6

print(b)
uh = np.linalg.solve(D, b)
#print(uh)
#tobj.show3dMeshData(uh)