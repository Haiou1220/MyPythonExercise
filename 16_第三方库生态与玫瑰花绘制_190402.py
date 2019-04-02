#*********************************************************************************************************************#
"""
9.2例子 --霍兰德人格分析雷达图
9.3从web解析到网络空间
9.4从人机交互到艺术设计
9.5例子--玫瑰花绘制
"""
#***********9.2例子 --霍兰德人格分析雷达图********
#霍兰德认为：人格兴趣与职业之间应有一种内在的对应关系
#人格分类：研究型。艺术型。社会型。企业型。传统型。现实型
#职业：工程师。实验员。艺术家。推销员。记事员。社会工作者
#matplotlib + numpy

"""
import  numpy as np
def npSum():
    a= np.array([0,1,2,3,4])
    b= np.array([9,8,7,6,5])
    c = a**2 + b**2
    return c
print(npSum())
"""
#**************9.3从web解析到网络空间*********
#requests:最友好的网络爬虫功能库
"""
import requests
r = requests.get("https://api.github.com/user",auth=("user","pass"))
r.status_code
r.headers["content-type"]
r.encoding
r.text
"""
#scrapy:优秀的网络爬虫框架，半成品功能
#pyspider 强大的web页面爬取系统
#beautiful soup ：HTML 和xml的解析库（与爬虫库scrapy requests 搭配使用）
#Re:正则表达式解析和处理功能库（是python的标准库）
"""
import re
r'\d{3}-\d{8}|\d{4}-\d{7}'
re.search()
re.match()
re.findall()
re.split()
re.sub()
"""
#python-goose：提取文章类型web页面的功能库

"""
form goose import Goose
url = "http://www.elmundo.es/elmundo/2012/10/28/espana/1351388909.html"
g = Goose({"use_meta_language":False,"target_language":"es"})
article = g.extract(url=url)
article.cleaned_text[:150]
"""
#********python库之web网站开发***************
#Django：最流行的web应用框架（后端）
    #MTV模式（模型模板视图）(与mvc不同)#

#pyramid：规模适中的web应用框架
"""
form wsgiref.simple_server import make_server
form pyramid.config import Configurator
from pyramid.response import  Response
def hello_world(request):
    return Response('Hello World')
if __name__ == "__main__":
    with Configurator() as config:
        config.add_route("hello","/")
        config.add_view(hello_world,route_name="hello")
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0",6543,app)
    server.server_forever()
"""

#flask:web应用开发微框架
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "hello,world"
"""
#（Djingo>Pyramid>Flask）

#********python库之网络应用开发***************
"""
WeRoBot:微信公众号开发框架（解析微信服务器以及反馈消息）
import werobot
robot = werobot.WeRoBot(token="tokenhere")
@robot.handler
def hello(message):
    return "hello world"
"""
#aip:百度AI开放平台接口
    #提供访问百度AI服务的python接口（语音.人脸.ORC.NLP.知识图谱.图象搜索）
#MyQR:二维码生成第三方库（艺术二维码。动态二维码）

#*********9.4从人机交互到艺术设计************
#*****图形用户界面，游戏开发，虚拟现实，图形艺术
#*****pyqt5:qt开发框架的pythonAPI接口
    #Qt是非常成熟的跨平台的GUI

#***图形用户界面***图形用户界面***
#*****wxPython:跨平台GUI开发框架
    #提供数据分析功能
"""
import wx
app = wx.App(False)
frame = wx.Frame(None,wx.ID_ANY,"Hello World")
app.MainLoop()
"""
#*****PyGObject:使用GTK+开发GUI的功能库
    #提供了整合GTK+，WebKitGTK+等库的功能
    #例如Anaconda就采用此框架构建GUI
"""
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
window = Gtk.Window(title="hello world")
window.show()
window.connect("destroy",Gtk.main_quit)
Gtk.main()
"""
#***游戏开发***游戏开发***
"""
PyGame:提供最简的游戏开发功能库（基于SDL）
Panda3D：开源·跨平台的3D渲染和游戏开发库
cocos2d:构建2D游戏和图形界面交互式应用框架
"""
#***虚拟现实***虚拟现实***
"""
VR Zero：在树莓派（微型电脑）上开发的VR应用的python库（支持设备的小型化，适合初学者）
pyovr:针对oculus VR设备的python库
vizard:通用VR开发引擎
"""

#***图形艺术***图形艺术***
"""
Quads:迭代的艺术（提供图片形成像素风）
ascii_art:ascii艺术库（图片输出成ASCII风格或者文本）
turtle:海龟绘图体系
"""
#************9.5例子--玫瑰花绘制************
"""
艺术：思想优先，编程是手段
设计：想法和编程同等重要
工程：编程优先，思想次之
"""
"""
编程不重要，思想才重要
认识自己：明确自己的目标，有自己的思想（想法）
方式方法：编程只是手段，熟练之，未雨绸缪为思想服务
为谁编程：将自身发展与祖国发展相结合，创造真正的价值
"""
#RoseDraw.py
import turtle as t
# 定义一个曲线绘制函数
def DegreeCurve(n, r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))
# 初始位置设定
s = 0.2 # size
t.setup(450*5*s, 750*5*s)
t.pencolor("black")
t.fillcolor("red")
t.speed(100)
t.penup()
t.goto(0, 900*s)
t.pendown()
# 绘制花朵形状
t.begin_fill()
t.circle(200*s,30)
DegreeCurve(60, 50*s)
t.circle(200*s,30)
DegreeCurve(4, 100*s)
t.circle(200*s,50)
DegreeCurve(50, 50*s)
t.circle(350*s,65)
DegreeCurve(40, 70*s)
t.circle(150*s,50)
DegreeCurve(20, 50*s, -1)
t.circle(400*s,60)
DegreeCurve(18, 50*s)
t.speed(10)
t.fd(250*s)
t.right(150)
t.circle(-500*s,12)
t.left(140)
t.circle(550*s,110)
t.left(27)
t.circle(650*s,100)
t.left(130)
t.circle(-300*s,20)
t.right(123)
t.circle(220*s,57)
t.end_fill()
# 绘制花枝形状
t.speed(90)
t.left(120)
t.fd(280*s)
t.left(115)
t.circle(300*s,33)
t.left(180)
t.circle(-300*s,33)
DegreeCurve(70, 225*s, -1)
t.circle(350*s,104)
t.left(90)
t.circle(200*s,105)
t.circle(-500*s,63)
t.penup()
t.goto(170*s,-30*s)
t.pendown()
t.left(160)
DegreeCurve(20, 2500*s)
DegreeCurve(220, 250*s, -1)
# 绘制一个绿色叶子
t.speed(10)
t.fillcolor('green')
t.penup()
t.goto(670*s,-180*s)
t.pendown()
t.right(140)
t.begin_fill()
t.circle(300*s,120)
t.left(60)
t.circle(300*s,120)
t.end_fill()
t.penup()
t.goto(180*s,-550*s)
t.pendown()
t.right(85)
t.circle(600*s,40)
# 绘制另一个绿色叶子
t.speed(10)
t.penup()
t.goto(-150*s,-1000*s)
t.pendown()
t.begin_fill()
t.rt(120)
t.circle(300*s,115)
t.left(75)
t.circle(300*s,100)
t.end_fill()
t.penup()
t.goto(430*s,-1070*s)
t.pendown()
t.right(30)
t.circle(-600*s,35)
t.done()





