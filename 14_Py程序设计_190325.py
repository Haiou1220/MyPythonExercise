#*********************************************************************************************************************#
"""
#8.1体育竞赛分析 --忽略
#8.2Python 程序设计思维 --忽略
    计算机思维（计算机的抽象相对与数学的抽象）
    API 不等于生态（生态是竞争）
    站在巨人的肩膀上LingTo:python123
    pip(python install package)
    pyPI的主站
#8.3第三方库的安装
1.pip安装
2.anaconda（非常适合python数据分析与数据展示）
3.文件安装（适用于要手动配置编译环境才可以安装）"""
"""
#8.4操作系统OS库之函数与进程管理
#******os.path子库（用以操作和处理文件路径）
#函数：abspath()返回绝对abs路径"""
# #
import  time as tm
import os.path as op
mytxtpath = op.abspath("../zfgzg.txt")
print(mytxtpath)

print(op.normpath("d://pye//file.txt"))#归一化，统一路径

print(op.realpath("c:://PYE//file.txt"))#相对路径
print(op.dirname("c://file.txt"))
print(op.basename("c://file.txt"))
print(op.join("d://","file.txt"))
print(op.exists("file.txt"))#判断当前文件是否存在
print(op.isdir("zfgzbg.txt"))#判断
print(op.isfile("zfgzbg.txt"))#判断

print(op.getatime("zfgzbg.txt"))#返回上一次访问acess时间
print(op.getmtime("zfgzbg.txt"))#返回modified访问时间
print(tm.ctime(op.getctime("zfgzbg.txt")))#返回creat访问时间

print((op.getsize("zfgzbg.txt")))#返回字节大小

"""
##############os库的进程管理##########
"""
#os.system(cmd)执行系统程序或者命令

import os
#os.system("C:\Windows\System32\calc.exe")#计算器
#os.system("C:\Windows\System32\mspaint.exe \
#         .\\cloud3.png")#画图

#环境参数（改变或者获取）
print(os.chdir("d://"))#改当前工作路径
print(os.getcwd())#获取当前Current 工作路径

print(os.getlogin())#用户信息
print(os.cpu_count())#cpu 环境

#随机字符串
print(os.urandom(10))#n个字节长度字符串，加密用途

"""
#8.5第三方库库自动安装
######自动脚本#########
"""
#如何用写程序 自动安装第三方库
"""
Numpy:N维数据表示与运算
Matplotlib 二维数据可视化
PIL 图形处理
Scikit-Learn :机器学习数据挖掘
Requests :网络爬虫以及HTTP
jieba :中文分词
Beautiful soup :html,xml 解析器
wheel 第三方库打包工具
pyinstaller 打包源代码位执行文件
Django py最流行的web框架
Flask 轻量级web框架
weRobot 微信机器人开发框架 
SymPy 数学符号计算工具
Pandas 高效数据分析和计算
Networkx 复杂网络和图结构建模与分析
pyQt5 基于qt的专业gui开发框架
pyOpenGL 多平台OpenGL开发接口
pyPDF2 PDF文件提取与处理
docopt py命令行解析
pyGame 简单小游戏开发框架

"""
#自动安装脚本--运行方法 命令行：python hello.py
#import os
libs = {"numpy","jieba","",""}#等等第三方库
try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Successful = " + lib)

except:
    print("Failed Somehow =" + lib)

#编写脚本调用已有程序
#配置文件+脚本程序，更加好（引擎+配置）





