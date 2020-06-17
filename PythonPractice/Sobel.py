import os
from PIL import Image
from skimage import img_as_float
import numpy as np
ImgPath='E:/SR/Data/NewResult/Test/'
ImgName=os.listdir(ImgPath)
filterX=[[-1, -2, -1],
         [0, 0, 0],
         [1, 2, 1]]
filterY=[[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]]
Data=np.zeros((len(ImgName),2))
for i in range(len(ImgName)):
    Img=Image.open(ImgPath+ImgName[i])
    Img=img_as_float(Img)
    a,b,c=Img.shape
    S = np.zeros((96, 96, 3))
    for j in range(3):
        SImg = Img[:, :, j]
        for m in range(1, (a-1)):
            for n in range(1, (b-1)):
                aa=SImg[m-1:m+1, n-1:n+1]
                pp=aa.shape
                Dx = filterX * SImg[m-1:m+2, n-1:n+2]
                Dy = filterY * SImg[m - 1:m + 2, n - 1: n + 2]
                S[m - 1, n - 1, j] = np.sqrt((sum(sum(Dx))) ^ 2 + (sum(sum(Dy))) ^ 2)
    Data[i, 1] = np.mean(S)
    Data[i, 2] = np.var(S)
