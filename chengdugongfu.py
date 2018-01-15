from appium import webdriver
import time
import os
import platform
import tempfile
import shutil
#from PIL import Image
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='4.4.2'
desired_caps['deviceName']='621QECPQ2BJWF'# adb devices查到的设备名
desired_caps['appPackage']='com.cditv.whxxapp'# 被测App的包名
desired_caps['appActivity']='.ui.act.WelcomeActivity'# 启动时的Activity
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(20)
driver.find_element_by_name("手机号").send_keys('13600000000')
driver.find_element_by_name("密码").send_keys('123456')
driver.find_element_by_name("登录").click()
if  driver.find_element_by_name("立即检测"):#等于1说明该name能被找到
    driver.find_element_by_name("立即检测").click()
    driver.get_screenshot_as_file( "D:\jietu\\立即检测.jpg")
    driver.find_element_by_name("服务设施建设").click()
    time.sleep(1)
    driver.get_screenshot_as_file( "D:\jietu\\服务设施建设.jpg")
    driver.find_element_by_id("com.cditv.whxxapp:id/title_left").click()#返回，将返回作一个公共的类
    time.sleep(1)
    driver.find_element_by_id("com.cditv.whxxapp:id/title_left").click()
else:
    driver.get_screenshot_as_file("d:\jietu\\检测错误截图.jpg")

def getSize():#获取手机屏幕大小
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)
l=getSize();
print(l)
def swipeDown(t):#没有看到效果
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
swipeDown(7000)
def swipeUp(t):#向上滑动
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.85)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    driver.swipe(x1, y1, x1, y2,t)
swipeUp(15600)

def swipLeft(t):#屏幕的左边就是我们的右手边
    l=getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,t)
swipLeft(1000)
def swipRight(t):
    l=getSize()
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    driver.swipe(x1,y1,x2,y1,t)
swipRight(1000)
