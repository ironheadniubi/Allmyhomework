# 存一个字典，key 为日期，value 为 1 or 0 1为节假日，0为非节假日
import datetime
import json
starttime=datetime.date(2016,5,1)

s = "1605"
datedic = {}
for i in range(1,32):
    snum = "%02d"%i

    today = starttime.replace(day=i)
    if today.weekday()+1==6 or today.weekday()+1==7:
        holiday=1
    else:
        holiday=0
    datedic[s+snum]=holiday
    #print(today)
    #print(today.weekday()+1)
#chaxun='160512'
#print(datedic[chaxun])
with open('holiday.json','w') as f:
    json.dump(datedic,f)