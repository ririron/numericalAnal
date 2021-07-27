import HandleMesh
import numpy as np
import matplotlib.pyplot as plt


mesh = HandleMesh.HandleMesh("R5")
p2p = mesh.getPoint2Point()

mesh.showMeshData()