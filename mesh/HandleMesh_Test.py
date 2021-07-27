import HandleMesh
import numpy as np

def saddle_func(x, y):
    return (x-0.5)**2 - (y-0.5)**2


tobj = HandleMesh.HandleMesh("R5")
p2p  = tobj.getPoint2Point() 
print(np.shape(p2p))

val = saddle_func(tobj.n2c[:,0], tobj.n2c[:,1])

tobj.show3dMeshData(val)
