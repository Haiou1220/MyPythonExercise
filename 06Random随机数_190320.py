####################################################################
#随机数random
#基本seek random(生成[0.0--1.0)的数,默认seek是系统时间)
#扩展randint(a,b)--uniform(a,b)随机小数，getrandbits(k)k比特长的整数

import random as rd

for i in range(10):
    print("{:2.0f}".format(rd.random()*10),end="\t")#随机数（0.0--1.0）
    #print((rd.random()*10))
print("\n"+"#"*50)


for i in range(10):
    print(rd.randint(10,100),end="\t")#整数范围a到b
print("\n"+"#"*50)

for i in range(5):
    print(rd.randrange(100,1000,2),end="\t")#随机数的范围以及步长,同for_range
print("\n"+"#"*50)
####################################################################
#随机数random
#基本seek random(生成[0.0--1.0)的数,默认seek是系统时间)
#扩展randint(a,b)--uniform(a,b)随机小数，getrandbits(k)k比特长的整数

import random as rd
print("返回k比特长(bit)的随机数(4bit=0-15)")
for i in range(10):
    print(rd.getrandbits(4),end="\t")#返回k比特长(bit)的随机数(4bit=0-15)
print("\n"+"*"*50)
###############################
for i in range(10):
    print("{:3.1f}".format(rd.uniform(10,20)),end="\t")#返回a-b的小数
print("\n"+"*"*50)
###############################
print("列表中选择一个")
print(rd.choice([1,2,3,4,5,6,7,8,9,]))#在seq序列中随机选择一个
print("字符串中选择一个")
print(rd.choice("asdfghjk"))#在seq序列中随机选择一个
###############################
print("#shuffle洗牌")
s= [11,12,13,14,15,16,17,18,19,]
rd.shuffle(s)#shuffle洗牌(;分号可以连接两语句)
print(s)
###############################


####################################################################