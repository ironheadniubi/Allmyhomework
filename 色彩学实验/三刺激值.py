import xlrd # 导入处理excel的库
book = xlrd.open_workbook('反射率.xlsx')   #打开反射率表格
book1 = xlrd.open_workbook("相对光谱率分布.xlsx")   #打开相对光谱率分布表格
sheet = book1.sheet_by_index(0) #读取相对光谱率分布表格的第一个sheet
sheet1 = book.sheet_by_index(0) # 读取反射率表格的第一个sheet
ans = 0
for i in range(0,len(sheet.col_values(2))):
    ans=ans+(sheet.col_values(2)[i]*sheet.col_values(4)[i])# Y = K*s(r)*y(r) 求积分相加的形式

k = 100 / ans # Y=100 求K
X = 0
Y = 0
Z = 0
for i in range(0,len(sheet1.col_values(0))):
    X = X+(sheet.col_values(4)[i]*sheet.col_values(1)[i]*sheet1.col_values(1)[i])
    Y = Y+(sheet.col_values(4)[i]*sheet.col_values(2)[i]*sheet1.col_values(1)[i])
    Z = Z+(sheet.col_values(4)[i]*sheet.col_values(3)[i]*sheet1.col_values(1)[i])
X = X * k
Y = Y * k
Z = Z * k
print(X,Y,Z)