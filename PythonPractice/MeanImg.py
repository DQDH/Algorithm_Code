import os
import numpy as np
from PIL import Image
from skimage import img_as_float
ImgPath='E:/SR/Data/DIV2K-train10000/X1Crop96Kmeans9900/3/'
ImgName=os.listdir(ImgPath)
Num=len(ImgName)
Sum1=np.zeros((96, 96, 3))
for i in range(Num):
    Img=Image.open(ImgPath+ImgName[i])

    Img=img_as_float(Img)
    a = Img.shape[2];
    b=a[2];
    Sum1=Sum1+Img
Sum2=Sum1.sum(axis=0)
Sum=np.sum(Sum2.sum(axis=1))
mean=Sum/(Num*96*96*3)
print('平均值为：', mean*255)