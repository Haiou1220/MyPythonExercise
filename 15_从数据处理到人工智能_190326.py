#*********************************************************************************************************************#
"""
9.1从数据处理到人工智能
9.2例子 --霍兰德人格分析雷达图
9.3从web解析到网络空间
9.4从人机交互到艺术设计
9.5例子--玫瑰花绘制
"""
#9.1从数据处理到人工智能
#数据表示-数据清洗（数据归一化等）-数据统计（中位数等）-
# 数据可视化（展示）-数据挖掘（分析其价值）-人工智能（深度分析与决策）
# **********#
#py库之数据分析
# Numpy：表示N维数组的最基础库
# 是数据分析与科学计算的基础库，支撑pandas
# 提供功能如 矩阵运算，广播函数，线性代数
# *********#
"""
#使用Numpy代替列表存储数据以及操作数据
"""
def pysum():
    a = [1,2,3,4]
    b = [4,3,2,1]
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return  c
print(pysum())#两数组（向量相加，对于x,y,z相加即可）

"""Numpy 表示数组（向量）的操作
其最小单元是数组，数组就是变量
"""
import  numpy as np
def npSum():
    a = np.array([1,2,3,4])
    b = np.array([4,3,2,1])
    c = a**2 + b**3#向量的平方+向量的立方是什么意思
    return c

print(npSum())

"""
*******py库之数据分析
pandas库（基于numpy）提供高级的数据分析功能（扩展了numpy）
数据类型与索引的关系，操作索引即操作数据
series = index + 一维数据
dataframe = index-row-Colum + 二维数据

scipy ：数学·科学和工程计算功能库
类似matlab 可以实现傅里叶’信号处理等应用
（傅里叶-信号处理-线性代数-图像处理-稀疏图）

*******py库之数据可视化
Matpoltlib：二维数据可视化功能库
其中子库matpoltlib.pyplot 用以可视化函数API
http://matplotlib.org

seaborn:统计类数据可视化功能库（基于matplotlib开发，支持numpy·pandas）
提供统计类数据可视化展示
主要展示数据间的分布·分类和线性分析等

Mayavi:三维科学数据可视化（最主要的三维库）

*******py库之文本处理
PyPDF2：用来处理pdf文件的工具集

NLTK:自然语言文本处理第三方库
-提供了一批简单易用的自然语言文本处理功能
-支持语言文本分类·标记·语法句法·语义分析等

Python-docx:创建或者更新Microsoft Word 文件的第三方库
--提供创建或者更新doc`docx文件的计算功能


"""

#PyPDF2：例子
from PyPDF2 import  PdfFileReader,PdfFileMerger
merger = PdfFileMerger()#对象
input1 = open("document1.pdf","rb")
input2 = open("document2.pdf","rb")
merger.append(fileobj= input1)#pages= (0,3)
merger.merge(position=2,fileobj= input2,pages=(0,1))
output = open("document-output.pdf","wb")
merger.write(output)

#ok 合并成功

#例子：NLTK:自然语言文本处理第三方库(最优秀)
"""
from nltk.corpus import treebank
t = treebank.parsed_sents("wsj_0002.mrg")[0]
t.draw()
"""
#Python-docx 例子:
"""
import  docx
document = docx.newdocument()
document.add_heading("Document Tiltle",0)
p = document.add_paragraph("A plain paragraph having some")
document.add_page_break()
document.save("demo.docx")
"""

"""
*******py库之机器学习
scikit-learn：机器学习工具集
最优秀的python第三方库
提供聚类·分类·回归·强化学习等计算功能

Tensor flow：谷歌开源机器学习框架
以数据流作为基础，图节点代表运算，边代表张量


"""
"""
import  tensorflow as tf
init = tf.global_variables_initializer()
sess = tf.Session()
sees.run(init)
res = sess.run(result)
print("result:",res)
#https://www.tensorflow.org 学习里面的例子
"""

"""
MXNet:基于神经网络的深度学习计算框架（py最重要的深度学习框架）
--提供可扩展的神经网络以及深度学习计算功能
--可用于自动驾驶·机器翻译·语音识别等众多领域
https://mxnet.incubator.apache.org
"""




