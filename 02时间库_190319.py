######################################################################
#时间库
#perf_counter(),Performance执行CPU计算器
##sleep休眠函数单位秒


import  time
sum1 = 0
stat = time.perf_counter()
for i in range(360):
    y = pow(2,i)
    sum1 +=y
print("{:e}".format(sum1))
end = time.perf_counter()
print("Performance time:{:.20f}".format(end-stat))

for i in range(10):
    time.sleep(1)
    print(i,end="\t")
print("Count Ok")
######################################################################
#时间格式化
#gmtime()GMT格林威治时间
#%Y 年份 ，%m 月份，%B 月份名称，%b 月份缩写
# %d 日期 ，%A 星期，%a 星期缩写
# H/h(12h)，%p(AM/PM)，%M(min)，%S(sec)，
#strftime(),,string format
#time() 时间戳
#ctime()
import  time
str1 = "2017/02/14,Monday,17:38:18"
#print(time.strftime("%Y/%m/%d,%A,%H:%M:%S",time.gmtime()))#相反作用函数strptime()

str_time = time.gmtime()#struct_time,非字符串
print("NOW_TIME:",end="")
print( str_time )#struct_time,非字符串

print(time.strptime(str1,"%Y/%m/%d,%A,%H:%M:%S"))#返回struct_time
print(time.time())  #gmt秒
print("Now:"+time.ctime())#Convert 转换了的时间,字符串
######################################################################











