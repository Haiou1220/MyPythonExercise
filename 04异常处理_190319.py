####################################################################
#异常try
try:
    a = eval(input("输入一个数\n"))
    print(a)
except NameError:
    print("输入错误")

####################################################################
#finally一定执行
#else 不发生异常执行
#except 有异常执行
try:
    num = eval( input("输入一个数字\n") )
    num0 = 1/num
except:
    print("输入无效数字或者输入零")
else:
    print("输入返回结果：{:5.2f}".format(num0))
finally:
    print("try_finall始终要执行")
print("try_结束")

####################################################################
#or 逻辑或，and 逻辑与 ,not 逻辑否
####################################################################
#if-else的变种
#（紧凑结构）<表达式1> if<条件> else<表达式2>
try:
    ok = eval(input("输入0错1对\n"))
except:
    print("输入错误")
else:
    print("对" if (ok==1)else "错")
####################################################################
#if与else
#if与elif
try:
    a = eval(input(\
        "听话：输入一个大于等于10的数，不听话：输入小于等于0的数\n"))
except:
    print("输入错误")
else:
    if(a>=10):
        print("你很听话")
    elif(a<=0):
        print("你不听话")
    else:
        print("不守规矩，是个天才")
print("end")
####################################################################







