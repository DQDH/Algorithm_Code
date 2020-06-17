import os
from PIL import Image
from skimage import img_as_float,img_as_ubyte
from scipy.misc import imsave

ImgPath1 = 'E:/SR/Data/Result/Texture/X4Crop96_9900/Set14/1/2-1/'
ImgPath2 = 'E:/SR/Data/Result/Texture/X4Crop96_9900/Set14/2/2-1/'
ImgPath3 = 'E:/SR/Data/Result/Texture/X4Crop96_9900/Set14/3/2-1/'
SavePath = 'E:/SR/Data/Result/Texture/X4Crop96_9900/Set14/1+2+3py/'
if not os.path.exists(SavePath):
    os.mkdir(SavePath)
ImgName1=os.listdir(ImgPath1)
ImgName2=os.listdir(ImgPath2)
ImgName3=os.listdir(ImgPath3)
Num=len(ImgName1)
for i in range(Num-1):
    Img1 = Image.open(ImgPath1 + ImgName1[i])
    Img2 = Image.open(ImgPath2 + ImgName2[i])
    Img3 = Image.open(ImgPath3 + ImgName3[i])

    Img = img_as_float(Img1)+img_as_float(Img2)+img_as_float(Img3)

    Img = Img/3
    Img = img_as_ubyte(Img)

    imsave(SavePath+ImgName1[i], Img)
    # Img.show()