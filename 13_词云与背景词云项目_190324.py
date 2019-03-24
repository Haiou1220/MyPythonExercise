#*********************************************************************************************************************#

###############7.5词云wordcloud#########################
#重要重要函数 " ".join(list_oject)-->str_oject

print("############################我的词频统计水浒传#######################")
import  jieba as jb
#打开文件
txt_str = open("zfgzbg.txt",mode="r",encoding="utf-8").read()
jb.add_word("海欧")
#剪词
mychinestword_list = jb.lcut(txt_str)#jb.lcut(txt_str)

#统计
chinest_dict = {}
performance_list =[]
for lt in mychinestword_list:
    if 1 == lt.__len__():#不统计标点符号
        continue

    elif lt in {"一个","一只","","","",""} :#不统计集合
        continue


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
print("############################################################词云 提QU重复性高的词语##################")
import  random as rd
meiwen_fd = open("meiwen1111.txt",mode="wt")
str_word_list = []
for i_len in range( chinesttuple_list.__len__()):
    word_time = chinesttuple_list[i_len][1]#元组第二个元素：出现次数
    if(word_time<=1):#筛选出现次数
        continue
    word_get = chinesttuple_list[i_len][0]  # 元组第一个元素：词 是字符串
    for i_word_add in range(word_time):
        str_word_list.append(word_get)
        meiwen_fd.write(word_get)


print("############################################################词云 提取重复性高的词语##################")
#打印前N
most_pers_set = set()#集合，前n出现次数排名
for i in range(400):#前n出现次数排名
    word1,num1 = chinesttuple_list[i]
    most_pers_set.add(word1)#添加进集合
    print("{0:4}:{1:4}".format(word1,num1))


#遍历词库list
performance_list.reverse()#反转顺序
for_len = performance_list.__len__()#全部单词长度

#print(most_pers_set)#debug
print("############################")#debug
perf_have_show_set = set()#创建现在已经的出场的人物集合
not_person_set = set()#非人物集
not_person_set={"二人","不可","将军","却说","荆州","商议","不能","","","军士","",\
                "人马","","","一人","大喜","次日","于是","引兵","陛下","","","都督","主公",\
                "后主","汉中","只见","大叫","众将","军马","不知","上马","太守","此人","","","","",""}
#去除非人物集合
most_pers_set=most_pers_set-not_person_set
"""打印高频单词 出场顺序
for i in range(for_len):
    performance_now = performance_list.pop()
    if ( performance_now in most_pers_set):

        if(performance_now  not in perf_have_show_set):
            # 添加已经出现的出场顺序set以排除重复
            perf_have_show_set.add(performance_now)
            #
            print("{0:3}:{1:4}".format(performance_now,chinest_dict[performance_now]))  # performance_person

"""

###############7.5词云wordcloud#########################
####MAKS参数
#from scipy.misc import imread
#mk = imread("")
####mask参数
print("###############7.5词云wordcloud###############")
#Wordcloud对象--生成对象 w= wordcloud.WordCloud()
#方法--generate（）加载文本；to_image()输出文件
#配置对象参数
"""width=400,height=200,
max_font_size = None,min_font_size=4,font_step=1,
font_path=None,(字体路径，中文要指定微软雅黑msyh.ttc)
max_words = 200,
stopwords=None,(排除单词列表，集合给出)
mask=None, （词云形状
from  scipy.misc import imread
mk = imread("pic.png")
mask = mk
）"""
"""background_color = 'black',


                   ranks_only=None, prefer_horizontal=.9, scale=1,
                 color_func=None, max_words=200, min_font_size=4,
                 stopwords=None, random_state=None,
                 max_font_size=None,mode="RGB",
                 relative_scaling='auto', regexp=None, collocations=True,
                 colormap=None, normalize_plurals=True, contour_width=0,
                 contour_color='black', repeat=False，margin=2,margin=2,
#配置对象参数"""
import wordcloud as wc

w = wc.WordCloud(width=1920,height=1920,font_path="msyh.ttc",max_font_size=3*100,background_color='white',max_words = 400)
fd_cloud = open("meiwen1931.txt",encoding="utf-8",mode="r+")
str_open = fd_cloud.read()
str_cloud =[]
for tet in str_open:
    str_cloud.append(tet)

#print(str_open)
rd.shuffle(str_word_list)
w.generate(" ".join(str_word_list))       #傻逼方法#str(str_word_list).replace("'","").replace(",",""))

#w.generate("Python and WordCloud")
w.to_file("cloud3.png")
w.to_image()


print(" ".join(str_word_list))
#print((str_word_list))#str(str_word_list).replace("'","*").replace(",","*"))傻逼方法
list_ran = ["aaa","sd","sdfg"]
print(list_ran)


#改进微信背景词云
#删除：
