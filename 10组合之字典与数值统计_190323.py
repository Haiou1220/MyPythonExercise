#*********************************************************************************************************************#
#6.3##############基本统计值############
#属性：有总个数，求和，平均数，方差，中位数，。。
"""
def getNum():
    nums = []
    iNumStr = input("请输入一个数字，回车确认")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr =  input("请输入数字，回车确认或者退出")
    return nums

print(getNum())
"""
##############
#求平均值

def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return  s/len(numbers)
"""print("平均值为：",mean( (1,2,3,4,5,6,7,8,9) ))
print("平均值为：",mean( [1,2,3,4,5,6,7,8,9] ))"""

#方差：差的平方和的平均再开方
def dev(numbers):
    n_mean = mean(numbers)
    print("numbers of len()=",len(numbers))
    sdev = 0.0
    for num in numbers:
        sdev = sdev +(num-n_mean)**2
        return pow(sdev/(len(numbers)),0.5)
print("方差=",dev([1,2,3,4,5,6,7,8,9]))

#中位数(//整数除法，sorted()小到大排序)
def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size%2 == 0: #偶数
        med = ( numbers[(size//2)-1] + numbers[size//2] )/ 2

    else:#奇数
        med = numbers[(size//2)]  #从零开始相当于加一

    return med

print("中位数:",median([1,2,3] )  )

#########################################################
##6.4组合数据-三大件之字典：#字典应用：映射的表达
#字典:->映射->键(索引)与值(数据)->属性与值
print("字典".center(44,"#"))
"""
序列之列表：通过index来获得数据
字典是键值对的集合，无序的,index是用户定义的

"""
#生成字典：{}或者dict() ,
di={'asd':"1",'fghj':"2"}
print(di['asd'])
#检查类型函数type()
ty1 = {}
ty2 = []
ty3 = {1,2}#空大括号保留给字典了
ty4 = set()#空大括号保留给字典了
print(type(ty1),type(ty2),type(ty3),type(ty4))
#方法
dic = {"country":"中国","city":"广州"}
print(dic.keys())
print(dic.values())
print(dic.items())
if ('country'in dic):
    print("'country'in dic():")
else:
    print("'country'not in dic:")
####
print("dit.get".center(44,"*"))
mydic = dic.get("country","不存在country")
print("dit.get=",mydic)

print(dic.pop("country","不存在，无法删除"))
print(dic.get("country","不存在country"))


print("随机取出item:{}并删除".format(dic.popitem()))
dic["language"]="普通话" #字典增加元素
print("字典呈现：{},字典长度:{}".format(dic,dic.__len__()) )




