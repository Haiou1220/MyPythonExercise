##############################################################
#函数函数函数

def fact_timeX(n,x=1):#阶乘(默认参数，）
    s = 1
    for i in range(1,n+1):
        s*=i
    return s

print(fact_timeX(4))

##################################################
def muti_puls(a,b,*c):#加法函数（可变参数)
    s2 = 0
    for i in c:#可变参数其实是元组
        s2 += i
    return s2+a+b

print(muti_puls(1,2,3,4,5,6,7,8,9))
##################################################
#函数传参，按参数赋值

def plus_fun(num,plus_step):
    return (num+plus_step)

print(plus_fun(plus_step=2,num=3))
##################################################
#函数返回多个值（元组类型，不可修改），[]列表可以修改，{}字典可以修改
print("函数返回多个值".center(40,"#"))
def return_allInputNum(*a):#可变参数其实是元组
    return a
def return_tow(a,b):
    return  a,b  #返回元组

print(return_allInputNum(1,2,3,4,5,6,7,8))

a,b= return_tow(98,89)
print(a,b)
print(return_tow(9,8))

##################################################
#全局变量与局部变量
#与c/c++语言不相同，局部同名的对象都是拷贝的（重名的组合数据类型也是拷贝）
#******************局部定义的变量就是局部的，用全局的就是拷贝的
print("全局变量与局部变量".center(44,"#"))
jubu1 = 1
jubu_s = '123456'

def fun_modif_jubu():
    jubu1 = 2       #这是在定义局部变量
    jubu_s = "abcde"#这是在定义局部变量
    return  jubu1,jubu_s
def fun_return_jubu():
    return   jubu1,jubu_s #返回全局（局部无定义）
###########################

list1 = [1,2,3,4,5]
def fun_modif_ok():
    list1.append(8)
    return list1

print("原来的jubu1,jubu_s",end=":");print(jubu1,jubu_s)
fun_modif_jubu()#修改无效
print("函数fun_modif_jubu返回：",end=":");print(fun_modif_jubu())
print("函数返回全局的jubu1,jubu_s",end=":");print(fun_return_jubu())


print("原来的组合类型list1",end=":");print(list1)
print("拷贝修改再返回",end=":");print(fun_modif_ok())
####################################
#lambda函数 不用def定义 用表达式定义
#lambda适用于函数的回调函数定义
print("lambda函数 ".center(44,"#"))
f = lambda x,y:x+y
f1 = lambda :"lambda_表达式"
print(f(1,2))
print(f1())
####################################
print("global,g1 = 1".center(44,"#"))
g1 = 1
def g_fun():#修改全局变量
    global g1
    g1 = 2

g_fun()
print("修改了全局变量g1={}".format(g1) )

##############################################################
####################################################
#递归=基例+链条
#递归（字符串反转）
def str_rev(s):
    if s =="":
        return s#空字符串
    else:
        return (str_rev(s[1:])+s[0])
print(str_rev("12345"))
####################################################
#斐波那契数列
#1-->1,2-->1,else_num--->(n-1)+(n-2)

def fbnq(n):
    if n==1:
        return 1
    elif n==2:
        return  1
    else:
        return (fbnq(n-1)+fbnq(n-2))

print(fbnq(16))
####################################################
#汉诺塔与k科赫曲线雪花（难点）
"""
print("#汉诺塔".center(44,'*'))
count_hnt = 0
def hnt(n):
    global count_hnt
    if(n==1):#假设是 原来塔的最大饼，搬到目标柱子
        count_hnt+=1


    else:#假设不是 塔的最大饼
         hnt(n-1)#且搬运上面n-1的全部饼到过度柱子
         #搬运n-1完成次数
         count_hnt += 1#最低的饼，搬到目标柱子
hnt(3)
print(count_hnt)
"""
####################################################
#pyinstaller 打包程序
####################################################
