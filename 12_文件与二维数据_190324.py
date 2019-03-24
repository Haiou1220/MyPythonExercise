#*********************************************************************************************************************#
##7.1文件操作
'''
二进制文件，文本文件（有字符编码，utf-8）
文本文件就是长的字符串
'''
"""
#创建文件写入文本"a+""+是读写"
str_txt = "./22.txt"
fd = open(str_txt,mode="a")#a是追加模式
#fd.write("\nasgdfhgjsdcfvgh")
#fd.write("\n1234567")
fd.writelines("\n"+input("one line:"))#从键盘输入
fd.writelines(["中国","广东"])
fd.close()
#打开文件读取
fd = open(str_txt,mode="rt")

tet = " "#循环读字符串
while tet!="":
    tet = fd.readline()

    print(tet,end="")

#关闭

fd.close()
"""
#读写附加符号+
#w+写&&读
fd1 = open("out.txt","w+")#open
fd1.writelines(["中国","广州","上海"])#写入
fd1.writelines("\n中国是个好国家")#写入
fd1.seek(0)#把指针移动到最前
w_puls_txt = fd1.readline()#读，，方法一
print(w_puls_txt)

###:#方法二:#方法二
fd1.seek(0)#把指针移动到最前
for line in fd1:#方法二#line现在是字符串
    w_puls_txt = line#读
    print(w_puls_txt)
	
##########################################################################
#7.2自动绘制轨迹

import turtle as t
t.title("自动轨迹绘制")
t.setup(1000,1000,0,0)
t.pencolor("red")
t.pensize(5)

#数据读取     l(距离),rl（左右转），r(角度),rgb1,rgb2,rgb3
data_list = []
fd = open("data.txt")
"""
fd.writelines(
"100,1,90,1,0,0"
"200,1,90,0,1,0"
"300,1,90,0,0,1"
"400,1,90,1,1,0"
"500,1,90,0,1,1"
"600,1,90,1,0,1"
"700,1,90,0,0,0"
)
"""
for line in fd:#读一行
    line = line.replace("\n","")#去符号回车替换成空字符串
    print(line)
    #print(line.split(","))#line.split(",")返回字符串列表
    data_list.append(list(map(eval,line.split(","))))#列表中有列表
print(data_list)
fd.close()
#自动绘制
t.speed(100)
for i in range(data_list.__len__()):#元素个数
    t.pencolor(data_list[i][3],data_list[i][4],data_list[i][5])
    t.fd(data_list[i][0])
    if data_list[i][1]:
        t.right(data_list[i][2])
    else:
        t.left(data_list[i][2])
#t.done()#不关闭窗口


###############7.3一维数据表示与处理#########################
#一维数据与二维数据区别
#键值对可以表达复杂结构

#一维数据
#list1=[1,2,3,4,]
#set1={1,2,34,55}
list2="中国$美国$法国$英国".split("$")  #存储方式逗号与自定义美元符号
list3="ghh mei fa ying".split()#spiit参数空，默认空格分隔
#print(list3)

#一维数据写入
#list4 = ["我","爱","你"]
list4 = "woaini"
list5 = ["我","爱","你"]
print(list4)

print("**".join(list4))#字符串的join方法是返回字符串，返回的字符串的是
                        # 自定义的字符串所分隔的每一个序列的元素
print("**".join(list5))
#fd.write("**".join(list5))#写入文件



print("###############7.4二维数据表示与处理###############")
#表示：列表（复合列表）（大数据分析会使用其他高级方法存储）
list_list1 = [
    [10,11,12,13,14,15],
    [20,21,22,23,24,25]
]#两重for

#csv（comma -separated values）
#读csv数据
"""
fname = "./csv1.csv"
fo = open(fname)
ls_csv1 = []
for line in fo:
    line = line.replace("\n","")#空字符替换
    ls_csv1.append(line.split(","))#以逗号分隔字符串形成元素
fo.close()
print(ls_csv1)
"""
#写入csv数据
fd_csvout = open("./csv1out1.csv",mode="a+")
csv_out_li = [
    ["序号","姓名","学校","成绩"],
    ["1","郭海欧","武艺大学","88"],
    ["2","郭海鸥","华南理工大学","90"],
    ["3","郭海牛","暨南大学","89"]
]
"""方法一
for i in range(csv_out_li.__len__()):
    fd_csvout.write(",".join(csv_out_li[i])+"\n")#join()的参数是序列，以自定义字符加入，形成字符串
"""
#方法二
# #从列表遍历获取元素
for line in csv_out_li:
    fd_csvout.write(",".join(line)+"\n")

fd_csvout.close()

