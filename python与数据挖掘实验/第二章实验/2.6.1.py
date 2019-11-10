#冒泡排序实现排序
def maopao(mylist):
    for i in range(0,len(mylist)-1):
        for j in range(0,len(mylist)-i-1):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]

    return mylist
SList = [5,6,3,4,8,1,9,0,2]
print(maopao(SList))

