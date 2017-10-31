#!D:/Program Files/Python3.6.0/python 
# -*- coding: utf-8 -*-
import	os
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner import MonkeyImage
from com.android.monkeyrunner import MonkeyRunner

	device = MonkeyRunner.waitForConnection()

# 中文的apk名称monkeyrunner识别不了，请在运行脚本之前运行下CHCP 65001
path = 'C:\\Users\\lpp\\Desktop\\application' #apk文件夹的绝对路径，会自动安装该目录下的所有apk文件
item = '.apk'
# l = []
for x in os.listdir(path):
	if item in x and os.path.isfile(os.path.join(path,x)):
		device.installPackage(path+'\\'+x)
		# l.append(x)
		MonkeyRunner.sleep(15)
		print(x+'   install success')
print('all applications have been installed,thanks')






