import pandas as pd
import math
#1931
D50X0=96.42
D50Y0=100
D50Z0=82.51
#1964
D50X0=96.72
D50Y0=100
D50Z0=81.4
#1931
D65X0=95.04
D65Y0=100
D65Z0=108.88
#
Y0=100
x0 = 0.3101
y0=0.3162
X0 = x0*Y0/y0
Z0=(1-x0-y0)*Y0/y0
print(Y0,X0,Z0)
df = pd.read_excel("lab.xlsx")
Y = list()
X = list()
Z = list()
for i in range(0,df.shape[0]):
    Y.append(df.Y[i])
    X.append((df.x[i]*df.Y[i])/df.y[i])
    Z.append(((1-df.x[i]-df.y[i])*df.Y[i])/df.y[i])
L = list()
a = list()
b = list()
# 将Yxy转化为Lab
for i in range(0,len(Y)):
    L.append(116*pow((Y[i]/Y0),1/3)-16)
    a.append(500*(pow((X[i]/X0),1/3)-pow((Y[i]/Y0),1/3)))
    b.append(200*(pow((Y[i]/Y0),1/3)-pow((Z[i]/Z0),1/3)))
print('L值为',L)
print('a值为',a)
print('b值为',b)
dotaL = list()
dotaa = list()
dotab = list()
dotaEab = list()
for i in range(1,3):
    dotaL.append(L[i]-L[0])
    dotaa.append(a[i]-a[0])
    dotab.append(b[i]-b[0])
    dotaEab.append(math.sqrt(pow(L[i]-L[0],2)+pow(a[i]-a[0],2)+pow(b[i]-b[0],2)))
print("+++++++++++++色差++++++++++++++++++")

print("明度差dotaL:")
print(dotaL)
print("色度差:dotaa ")
print(dotaa)
print("色度差dotab")
print(dotab)
print("总色差:")
print(dotaEab)
print("+++++++++++++++++++++++++++++++++++")



# CMC(1:c) 色差公式
def CMC(L1,a1,b1,L2,a2,b2,l,c):
    C1 = math.sqrt(a1*a1+b1*b1)
    C2 = math.sqrt(a2*a2+b2*b2)
    dC=C1-C2
    dH = math.sqrt(pow((a1-a2),2)+pow((b1-b2),2)-dC*dC)
    dL=L1-L2
    da=a1-a2
    db=b1-b2
    if L1<16:
        SL=0.511
    else:
        SL=(0.040975*L1)/(1+0.01765*L1)
    SC = (0.0638*C1)/(1+0.0131*C1)+0.638
    F = math.sqrt(C1**4/(C1**4+1900))
    H = math.atan(b1/a1)
    if H>0:
        H1=H
    else:
        H1 = H+1
    if H1>=(164/360) and H1<=(345/360):
        T = 0.56+abs(0.2*math.cos(H1+168/360))
    else:
        T = 0.36+abs(0.4*math.cos(H1+35/360))
    SH = SC*(F*T+1-F)
    ans = math.sqrt((dL/(l*SL))**2+(dC/(c*SC))**2+(dH/SH)**2)
    return ans


print("++++++++++++++++CMC(2:1)色差++++++++++++++++")

print(CMC(L[0],a[0],b[0],L[1],a[1],b[1],2,1))
print(CMC(L[0],a[0],b[0],L[2],a[2],b[2],2,1))

print("++++++++++++++++++++++++++++++++++++++++++++")
















