##############################################################
#组合数据-三大件#
#1序列：列表，元组，
#2集合：集合
#3字典：字典
##############
#集合类型(无序)（不可修改）***********************************************
#用{}或者set{}，建立空集合set()
A = {"python",123,("py",456)}#元组可以放，因为是不可修改
print(A)
B = set("a1b2c3abc123")#字符串建立集合
C1 = set("def456")#字符串建立集合
C2 = set("abc123")
print(B)
#集合运算
"""
C1|C2
C1&C2
C1-C2
C1^C2
>=/<=(包含)
"""
#与=结合的运算
print("原来C1:",(C1))
C1|=C2#更新
print("更新C1:",(C1))
#集合方法
"""
c1=set("qwertyuiop")
c1.add()
c1.discard();c1.remove()(Exception)
c1.clear();c1.pop()(Exception)
c1.copy();c1.__len__();'a' in c1; 'a ' not in c1;
"""
#例子：数据去除
ls = ['p','p','y','y',123]
s = set(ls)
print("数据去除",s)
#ex:
set2list = list(s)
print("set转list ：",list(s))
########
#psss占位符
pass_s = set("pasS")
try:
    while True:
        pass_a = pass_s.pop()
        print(pass_a,end="-")
except:
    pass#空语句，占位

print("\npass_ok")

#################################
#序列类型的衍生：字符串，元组，列表
#序列类型（有序，向量，元素类型可以不同）(可以index)
#序列类型可以正反遍历
#序列操作符：
#x in s;x not in s;
#s+t(链接); s*time(copy);
# s[index];s[i:j:k]

print("##########序列###############");
li_l = ["456",2,'a',{"123",1}]
print(li_l[::-1]);print(li_l[::1]);#切片

#方法方法方法
print("##########序列-方法方法###############");
li_m = [1,2,2,2,3,4]
#les();
#min()(Exception);max()(Exception);#同类型才可以

print(li_m.index(2))#返回元素位置
print(li_m.count(2))
print(max(li_m));print(max("abcdefg"))
########################

#*****************元组*********************************************#
#元组元组元组元组tuple()/()创建
#可以不用小括号 return 1,2 #返回一个元组
print("############元组#################")
creature = "dog","cat","human"
creatures = ("mama","dada",creature)#元组里面有元组
print(creatures)
#元组有同样的序列操作方法（除修改操作）
print(creatures[-1][::1])#选中操作

#***********列表*********************************************#
#列表
#创建[]或者list()
#可以修改
print("#####列表#######")
lsls = ["abc",123]
lsls2 = lsls#列表赋值是引用（指针），因为lits是可以修改的

print(lsls2)
print(lsls)
lsls2[0] = "?"#其本质是char** 所以可以index到元素再修改
print(lsls2) #ls[i]="x" 或者高级的 ls[i:j:k] = lt
print(lsls)
print("###ls[i:j:k] = lt###")
ls_ijk = ["0",1,"2",3,"4"]
lt_ijk = [1,2,3,4,5,6,7,8,9]
ls_ijk [0:2:] = lt_ijk#遍历修改对于的index元素
print(ls_ijk)
#########
#del ls_ijk[0]#删除index
#del ls_ijk[0:2]#删除index范围
#ls+=lt;ls*3;
#ls_ijk.insert(2,7) #增加元素
 #('x' in ls_ijk ) #判断元素是否再list中
 #ls_ijk.index('x') #返回要求字符的index
ls_ijk1=[0,1,2,3,4,5,6,7,8,9]
print(ls_ijk1)
del ls_ijk1[::2]#删除选中的index元素
print(ls_ijk1)
print(ls_ijk1*2)
#方法
ls_ijk.append("append_love")#ls.clear,,ls.copy,,ls.insert,,
                                # ls.pop,,ls.remove,ls.reverse
print("ls_ijk.append:",ls_ijk)
'''#**********************************************####
总结三者的应用场景：元组适用于函数的返回值（及不可以修改），
列表是最灵活的 ，基于序列基类可以增删以及其他操作，


####**********************************************#'''

#********字符串*******************************************
# 字符串是基于序列基类#
#字符串是不可以修改
print("############字符串#####")
strstr = "str1:asd"
strstr1 ="str2:123456"

print(strstr)
print(strstr1)
strstr1 = strstr #字符串变量不能引用，是拷贝
#strstr[0] = '?'exeption #字符串的index不可以写入，只能读
print(strstr)
print(strstr1)
print(strstr1[1])#字符串index不可以写入，只能读


