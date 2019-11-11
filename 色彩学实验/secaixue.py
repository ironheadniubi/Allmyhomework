import pandas as pd
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_excel('ynasetixi.xlsx')
#print(df.Y)
# 验证H的不均匀性，若为均匀则每个相邻两个点之间点距离相等，我们判断有多少不相等点距离就可以了
ans = list()
#print(df.shape[0])
for i in range(0,23):
    ans.append(pow((df.x[i+1]-df.x[i]),2)+pow((df.y[i+1]-df.y[i]),2)+pow((df.z[i+1]-df.z[i]),2))
if len(set(ans))==1:
    print("china color system H is average")
else:
    print("china color system H is not average")
# 同理可以验证C的不均匀性
data = pd.read_excel("ynasetixi.xlsx",sheet_name="Sheet2")
ans2 = list()
for i in range(0,data.shape[0]-1):
    ans2.append(pow((data.x[i + 1] - data.x[i]), 2) + pow((data.y[i + 1] - data.y[i]), 2) + pow((data.z[i + 1] - data.z[i]), 2))
if len(set(ans2))==1:
    print("china color system C is average")
else:
    print("china color system C is not average")


fig = plt.figure()
ax = plt.subplot(111, projection='3d')
ax.scatter(df.x,df.y,df.z,c='y')
ax.scatter(data.x,data.y,data.z,c='g')
ax.set_title('China color system')
plt.show()