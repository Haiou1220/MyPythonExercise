####################################################################
#文本进度条
#单行刷新，数字进度条
#\r回车（re） \n换行（next） \t制表(table)

import  time
print("123456789",end="")
time.sleep(1) #等待一秒看效果
print("\r*",end="")#刷新覆盖之前,单行

print("\n")
print("****")#参考坐标

for i in range(101):
    time.sleep(0.1)
    print("\r{:3}%".format(i),end="")

print("\n****")#参考坐标
####################################################################
#我的进度条
import  time
scale  = 100
print("开始进度条")
print("*"*(scale+4))
for i in range(scale+1):#遍历
    str_start = "*"*i
    str_wait ="."*(scale-i)
    time.sleep(0.1)
    print("\r{:3d}%{}->{}".format( int((i/scale)*100),str_start,str_wait),end="")# xx%**********....................

print("\n")
print("结束进度条")
####################################################################
#文本进度条
#有时间统计，有方括号
import time

scale = 100
time_start = time.perf_counter()
print("进度条开始".center(scale+9,"="))
for i in range(scale+1):
    str_a ="*"*i
    str_b = "."*(scale-i)
    per_num = (i/scale)*100
    during = time.perf_counter() -time_start
    print("\r{:^3.0f}%[{:}->{:}]{:5.2f}s".format(per_num,str_a,str_b,during),end="")
    time.sleep(0.1)
print("\n"+"进度条结束".center(scale+9,"="))

####################################################################

####################################################################


####################################################################

####################################################################








