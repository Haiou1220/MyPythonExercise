################################################################
###https://www.bilibili.com/video/av42408424/?p=80############
#########嵩天PYTHON###########################################
################################################################
#求星期几---版本一
weekid = eval(  input(  "输入星期数字(1-7):\n"))

weeksrt = "星期一星期二星期三星期四星期五星期六星期日"

pos = (weekid -1)*3

str = weeksrt[pos:pos+3]

print(str )
####################################################################
#求星期几---版本二
weekid = eval(  input(  "输入星期数字(1-7):\n"))

weeksrt = "一二三四五六日"

str = weeksrt[weekid-1]

print("星期"+str )
#####################################################################
#字符串操作------1
str = "a,s,d,f,g,h,j,k,l"

print(str.count('a'))#计数

print(str.split(',' ))#以特定字符串间隔开，形成list

str2= str.replace('a','aa')#替换，返回字符串
print(str2)#替换，返回字符串

#####################################################################
#字符串操作------2
str = "GHH"
str1 = str.center(20,"*")#对其且填充
print(str1)

print(str1.strip("*="))#去除两端的特定字符

print(",".join("12345")) #迭代字符串添加特定字符

#####################################################################
#字符串操作------3
str1 = "123456"
print(str1.__len__())#求字符串长度
print(len("str"))#求字符串长度

str2 = str(3.14) #转字符串
print(str2) ######转字符串
print(eval(str2)+1) #评估函数，去字符串

list1 = [1,2,3,4]
print(str(list1))#转字符串
#####################################################################
print(hex(10))#十进制
print("o")
print(oct(10))#八进制octal
#####################################################################
#字符unincode
print("1+1=2"+chr(10004))#返回unincode字符

char1 = chr(9801)#返回unincode字符
print(char1)
print(ord(char1))#返回 字符的order编号
#####################################################################
#打印12星座，第一个星座9800

start_flag = [] #声明一个空列表
for i in range(9800,9800+12):
    start_flag.append( chr(i))
    print(chr(i),end="\t")#结束非换行，添加end字符

print("\n")
print(start_flag)
#####################################################################
#字符串与注释
str1 = '''这是一个双引号("),这是一个单引号(')'''
str2 = """这是一个双引号("),这是一个单引号(')"""

'''###############注释
print()
abs()
'''
str_zhushi = '''
注释开始
print()
abs()
注释结束
'''

print(str1)
print(str2)
print("这是一个注释:"+str_zhushi)
#####################################################################

#字符串序号的正反
#字符串的index索引与切片
#切片[M:N:K]
    # M与N至少填写一个表示至开头或者至结尾
    #K表示步长，可以省略表示index步长为正向1单位，可以为负，表示逆序
    #N是index不包括的
str_mnk = "abcdefghijk"

print(str_mnk[::2])#开始带结束，步长为二

print(str_mnk[::-1])#倒叙反转
#####################################################################
#格式化输出，模板字符串与槽
#格式化输出，模板字符串与槽
#(:)表示格式控制标记的引导符号
#填充，对齐，宽度，    <,>数字的千位分隔符，<.>精度，<类型>(f,d,o,x,e,b,c)
str_form = "{0}:计算机{2:*^07}号的CPU占用率为{1:02d}%，工作电压为{3:08.3f}V".format("2019/03/18",9,7,5.010290342)

print( "{:,.2f}".format(12345.6789) ) #千位分隔符(必须是f格式)，浮点格式无宽度
print( "{:,.0f}".format(98765432) ) #千位分隔符(必须是f格式),可以解析整数
print( "{:*>12}".format(8765432) )
print("{0:b},{0:c},{0:d},{0:o},{0:x}".format(9800))
print(str_form)
#####################################################################