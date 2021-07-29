import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from numpy.lib.twodim_base import triu_indices_from
from numpy.lib.type_check import _common_type_dispatcher

class HandleMesh:
    
    """
    meshdataを扱うクラス
    """

    def __init__(self, fiName) :
        self.setMeshData(fiName)

    @staticmethod
    def readCSV(fiName):
        with open(fiName) as fi:
            reader = csv.reader(fi)
            data = [[float(d) if '.' in d else int(d) for d in row ] for row in reader ]
        return data

    @staticmethod
    def getFmArray(pt):

        T = np.abs(0.5 * ( (pt[1][0] - pt[0][0]) * (pt[2][1] - pt[0][1]) 
                            - (pt[2][0] - pt[0][0]) * (pt[1][1] - pt[0][1])))
        

        return (T / 12) * (np.ones((3, 3)) + np.identity(3))


    def setMeshData(self, fiName):

        self.n2c = np.array(self.readCSV(fiName + "_n2c.csv"))
        self.e2n = np.array(self.readCSV(fiName + "_e2n.csv"))
        self.b2n = np.array(self.readCSV(fiName + "_b2n.csv")) 
        
        self.pNum = np.shape(self.n2c)[0]

    def getPoint2Point(self):
        #格納する変数
        #[始点; 終点; 終点]
        p2p = np.zeros((np.shape(self.e2n)[0], np.shape(self.e2n)[1], 2))
        #-1の理由は，Pythonのインデックスの開始が0だから
        for i,p in enumerate(self.e2n):
            stInd = int(p[0]-1.0)
            stP   = self.n2c[stInd]
            p2p[i, 0, :] = stP
            for j,s in enumerate(p[1:]):
                enInd = int(s - 1.0)
                enP   = self.n2c[enInd]
                p2p[i, j+1, :] = enP 
        return p2p

    def getPoint2PointFor3d(self, zVal):
        #格納する変数
        #[始点; 終点; 終点]
        p2p = np.zeros((np.shape(self.e2n)[0], np.shape(self.e2n)[1], 3))
        if zVal == []:
            zVal = np.zeros(np.shape(self.n2c)[0])
        #-1の理由は，Pythonのインデックスの開始が0だから
        for i,p in enumerate(self.e2n):
            stInd = int(p[0]-1.0)
            stP   = self.n2c[stInd]
            p2p[i, 0, 0:2] = stP
            p2p[i, 0, 2]   = zVal[stInd]
            for j,s in enumerate(p[1:]):
                enInd = int(s - 1.0)
                enP   = self.n2c[enInd]
                p2p[i, j+1, 0:2] = enP 
                p2p[i, j+1, 2]   = zVal[enInd]   
        return p2p

    def getBoundaryEdge(self):

        edgeX = np.zeros((int(np.max(self.b2n[:,0])), 2))
        edgeY = np.zeros((int(np.max(self.b2n[:,0])), 2))
        

        for b in range(1, int(1.0 + np.max(self.b2n[:,0]))):
            stPind = int(np.min(self.b2n[self.b2n[:, 0] == b][:, 1:]) - 1.0)
            enPind = int(np.max(self.b2n[self.b2n[:, 0] == b][:, 1:]) - 1.0)

            edgeX[b-1, 0] = self.n2c[stPind, 1]
            edgeX[b-1, 1] = self.n2c[enPind, 1]

            edgeY[b-1, 0] = self.n2c[stPind, 0]
            edgeY[b-1, 1] = self.n2c[enPind, 0]

        return edgeX, edgeY
        

    def showMeshData(self):
        #まずは点だけ
        for i,p in enumerate(self.n2c):
            #plt.scatter(p[0], p[1])
            plt.annotate(i, [p[0], p[1]])
        #点を結ぶ
        #エッジの取得
        p2p = self.getPoint2Point()
        #エッジのプロット
        for line in p2p:
            stP = line[0]
            for p in line[1:]:
                cx = [stP[1], p[1]]
                cy = [stP[0], p[0]]

                plt.plot(cy, cx, "gray")
        #領域のプロット
        for i,line in enumerate(p2p):
            triX = (line[0, 1] + line[1, 1] + line[2, 1]) / 3
            triY = (line[0, 0] + line[1, 0] + line[2, 0]) / 3

            plt.annotate(i, [triY, triX])
        #境界のプロット
        edgeX, edgeY = self.getBoundaryEdge()
        for i in range(np.shape(edgeX)[0]):
            plt.plot(edgeY[i], edgeX[i])
    
        plt.show()
    
    def show3dMeshData(self, cz):
        
        #エッジの取得
        p2p = self.getPoint2PointFor3d(cz)
    

        fig = plt.figure()
        ax = Axes3D(fig)
       
        ax.add_collection3d(Poly3DCollection(p2p))
        ax.set_zlim(-0.2, 0.2)
        plt.show()