#*********************************************************************************************************************#
####################6.5——jieba库#####################
"""
pycharm的变量提示符号：
p：parameter
m：method 
c：class
v：variable
f：function 
"""
#6.5jieba词库实战
#常用函数:
# lcut()返回list
#jb.lcut_for_search
#add_word()
import jieba as jb

print("返回精确模式下的list,无冗余：\n",jb.lcut("中华人民共和国是一个伟大的国家"))
print("返回全模式下的list,有冗余：\n",jb.lcut("中华人民共和国是一个伟大的国家",cut_all = True))

print("返回搜索引擎模式下的list,有冗余：\n",jb.lcut_for_search("中华人民共和国是一个伟大的国家"))

jb.add_word("郭海鸥")
print(jb.lcut("中国是郭海鸥的国家"))

####################6.6——词频统计#########################################
#https://python123.io/resources/pye/hamlet.txt
#https://python123.io/resources/pye/threekingdoms.txt
#步骤1归一化：
# open()一个英文文本文件
# 变变文本为小写
# 使用文本函数replace（）替换各种符号为空格---形成字符串列表
##步骤2获得单词列表：
# 使用字符串函数split（）以空格分隔字符串并返回字符串列表
# 往字典中添加出现次数的值
# 字典键值对转列表
# 列表排序,按照元素里面的第二个子元素sort
##步骤2获得单词列表：
# 打印前十个单词统计#

mystr = "ghh love my famery"
mylist = mystr.split()#ok
print(mylist)
print("############list-sort#################")
dict2301 = {"fountry":2,"city":3,"anguage":6}
print("字典转换列表之前有冒号",dict2301)
#list2301 =  list(dict2301)#字典变量默认是字典的键
list2301 =  list(dict2301.items())#字典items是的键值对的元组
print("字典转换列表之后没有冒号：",list2301)#[('fountry', 2), ('city', 3), ('anguage', 6)]
list2301.sort(key=lambda x:x[1],reverse=True)#reverse是大到小,x是元组元素，x[1]是元组元素里面的第二个子元素
print("有排序：",list2301)
myword,wordtime = list2301[1]
print("{}---{}".format(myword,wordtime))


print("############我的词频统计hamlet##################################")
#导入jieba
#import  jieba as jb

def getTxt(txt_str):#"hamlet.txt"

    #打开txt文件
    mytextfd = open(txt_str,mode='r').read()#文件字符串操作

    mytextfd = mytextfd.lower()#小写字体

    # 去符号,建立序列的字符串
    unuser_charstr = """,./<>?;'":[]{}\\|-=_+`~!@#$%^&*()"""

    # 去非法字符
    for c1 in unuser_charstr:
        mytextfd = mytextfd.replace(c1, " ")
    """## 去除非法字符方法一
    #for index in range(len(mytextlist)):
     #   for c1 in charstr:
      #      if mytextlist[index] == c1:
      #          mytextlist[index] = " "
    """
    return  mytextfd

#归一化了#归一化了#归一化了
articlestr = getTxt("hamlet.txt")#归一化了

#以空格分割字符串，形成字符串列表
mywordlist = articlestr.split() #字符串操作，空格分隔形成list

#建立字典统计次数
myworddict = {}

#遍历list
for word in mywordlist:
    myworddict[word] = myworddict.get(word,0) + 1#获取指定键的值

#列表转换成复合列表
myword_tuple_list = list(myworddict.items())

#复合list排序(sort(key))
myword_tuple_list.sort(key=lambda  x:x[1],reverse=True)

#生成前N-M位(1-n++)的词频(单词&&次数)
def outRangword_frequency(star_1=0,end=10):
    global myword_tuple_list
    star = star_1 -1
    dict_word_fre = {}
    list_tuple = list()
    if end>len(myword_tuple_list):
         dict_word_fre["范围越界"] = end
         return  list(dict_word_fre.items())
    if star<=-1:
         dict_word_fre["范围越界"] = star
         return  list(dict_word_fre.items())
    for i in range(end-star):
        word , time = myword_tuple_list[star+i]
        dict_word_fre[word] = time

    list_tuple = list(dict_word_fre.items())
    return list_tuple


list_test = outRangword_frequency(2,11)#调整位置，范围
print(myword_tuple_list)#打印原始的元组列表

for i in range(list_test.__len__()):
    word1,time1 = list_test[i]
    print("{0:8}:{1:4}".format(word1,time1))


print(############################我的词频统计水浒传#######################)
import  jieba as jb
#打开文件
txt_str = open("threekingdoms.txt",mode="r",encoding="utf-8").read()
#剪词
mychinestword_list = jb.lcut(txt_str)
#统计
chinest_dict = {}
performance_list =[]
for lt in mychinestword_list:
    if 1 == lt.__len__():#不统计标点符号
        continue

    elif lt== "孔明曰" :
        lt = "孔明"
    elif lt== "关公" or lt== "云长" :
        lt = "关羽"
    elif lt== "玄德" or lt== "玄德曰":
        lt = "刘备"
    elif lt== "孟德" or lt== "丞相" :
        lt = "曹操"
    chinest_dict[lt] = chinest_dict.get(lt,0)+1
    performance_list.append(lt)#加入出场顺序

#字典转元组list
chinesttuple_list = list(chinest_dict.items())

#排序
chinesttuple_list.sort(key = lambda x:x[1],reverse=True)

#打印前10
most_pers_set = set()#集合，前n出现次数排名
for i in range(50):#前n出现次数排名
    word1,num1 = chinesttuple_list[i]
    most_pers_set.add(word1)#添加进集合
    #print("{0:4}:{1:4}".format(word1,num1))


#遍历词库list
performance_list.reverse()#反转顺序
for_len = performance_list.__len__()#全部单词长度

#print(most_pers_set)#debug
print("############################")#debug
perf_have_show_set = set()#创建现在已经的出场的人物集合
not_person_set = set()#非人物集
not_person_set={"二人","不可","将军","却说","荆州","商议","不能","如何","如此","军士","",\
                "人马","天下","左右","一人","大喜","次日","于是","引兵","陛下","今日","不敢","都督","主公",\
                "后主","汉中","只见","大叫","众将","军马","不知","上马","太守","此人","","","","",""}
#去除非人物集合
most_pers_set=most_pers_set-not_person_set

for i in range(for_len):
    performance_now = performance_list.pop()
    if ( performance_now in most_pers_set):

        if(performance_now  not in perf_have_show_set):
            # 添加已经出现的出场顺序set以排除重复
            perf_have_show_set.add(performance_now)
            #
            print("{0:3}:{1:4}".format(performance_now,chinest_dict[performance_now]))  # performance_person





