#################################################
#圆周率计算
#公式
pi = 0
pi_step =1000
for i in range(pi_step):
    pi+=(1/pow(16,i))*\
        ( (4/(8*i+1)) - (2/(8*i+4)) -(1/(8*i+5)) - (1/(8*i+6))  )
print("公式计算圆周率：{:}".format(pi) )

#蒙特卡洛方法(**是平方)
import  random as rd            #全部选择包里面的函数
from time import perf_counter #选择包中的函数
print("蒙特卡洛方法".center(30,"*"))
darts = 100*100 #投点数量
hits = 0
start_t = perf_counter()#开始time
for i in range(1,darts+1):
    x,y = rd.random(),rd.random()
    distan = pow( (x**2+y**2),0.5)#平方再开方
    if distan<=1.0:
        hits+=1

end_t = perf_counter()#结束time
pi_2 = 4*( hits/darts)
print("消耗时间:{1:.3f}s---算得结果:Pi={0:}".format(pi_2,end_t-start_t))

#################################################