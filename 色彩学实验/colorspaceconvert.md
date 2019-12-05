'''
1. 读取图片,用numpy存取rgb值
2. 利用公式rgb转化为RGB
3. 公式进行RGB to 不同色度空间的转换
4. 进行直方图的绘制
7. 代码的可移植性和可读性差,没时间优化和美化,将就看好了
'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
i = Image.open('flower.jpg')
iarrayrgb = np.array(i)
#print(iarrayrgb)
def gamma(x):
    if x>0.04045:
        return ((x+0.055)/1.055)**2.4
    else:
        return x/12.92
def rgb2RGB():
    R=iarrayrgb[:,:,0]
    for i in range(0,R.shape[0]):
        for j in range(0,R.shape[1]):
            gamma(R[i][j])
    G=iarrayrgb[:,:,1]
    for i in range(0, G.shape[0]):
        for j in range(0, G.shape[1]):
            gamma(G[i][j])
    B=iarrayrgb[:,:,2]
    for i in range(0, B.shape[0]):
        for j in range(0, B.shape[1]):
            gamma(B[i][j])

    return R,G,B
def RGB2YUV():
    R,G,B=rgb2RGB()
    y = 0.299*R+0.587*G+0.114*B
    u = -0.147*R-0.289*G+0.436*B
    v = 0.615*R-0.4515*G-0.1*B
    yuvarray = np.array([y,u,v],dtype=float)
    return yuvarray.reshape(240,180,3)

def RGB2YIQ():
    R,G,B =rgb2RGB()
    Y = 0.299*R+0.587*G+0.114*B
    I = 0.596*R-0.274*G-0.322*B
    Q = 0.211*R-0.522*G+0.311*B
    YIQarray = np.array([Y,I,Q],dtype=float)
    return YIQarray.reshape(240,180,3)
def RGB2YCbCr():
    R, G, B = rgb2RGB()
    Y = 0.299 * R + 0.587 * G + 0.114 * B
    Cb = -0.1687*R-0.3313*G+0.5*B+128
    Cr = 0.5*R-0.4187*G-0.0813*B+128
    YCbCr = np.array([Y,Cb,Cr],dtype=float)
    return YCbCr.reshape(240,180,3)

YUV = RGB2YUV()
print(YUV)

YIQ = RGB2YIQ()
print(YIQ)

YCbCr=RGB2YCbCr()
print(YCbCr)

# 直方图绘制
plt.figure()

ax1=plt.subplot(221)
ax1.set_title("YUV")
plt.hist(YUV.reshape(129600),256)

ax2 = plt.subplot(222)
ax2.set_title("YIQ")
plt.hist(YIQ.reshape(129600),256)

ax3 = plt.subplot(223)
ax3.set_title("YCbCr")
plt.hist(YCbCr.reshape(129600),256)

ax4 =plt.subplot(224)
ax4.set_title("rgb")
plt.hist(iarrayrgb.reshape(129600),256)
plt.tight_layout()
plt.show()