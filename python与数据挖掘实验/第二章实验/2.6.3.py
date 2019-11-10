# 读取文件练习
dataArr = []
labelarr = []
with open('horseColic.txt','r') as f:
    for line in f.readlines():
        Arr=[]
        line=line.strip()
        s = line.split("\t")
        Arr = s[:-1]
        dataArr.append(Arr)
        labelarr.append(s[-1])

print(dataArr[0:3])
print(labelarr[0:3])

