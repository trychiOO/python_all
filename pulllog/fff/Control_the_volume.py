#_*_ coding:utf-8 _*_
#author:yr
import pyautogui

import time
#
# import  os
# import  time
# import pyautogui as pag
# try:
#     while True:
#         print("Press Ctrl-C to end")
#         screenWidth, screenHeight = pag.size()  #获取屏幕的尺寸
#         print(screenWidth,screenHeight)
#         x,y = pag.position()   #获取当前鼠标的位置
#         posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
#                                         rjust()返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
#         print(posStr)
#         time.sleep(0.2)
#         os.system('cls')   #清楚屏幕
# except KeyboardInterrupt:
#     print('end....')





# #
#
xOffset =  1403
yOffset = 1047

num_seconds =  2

pyautogui.moveTo(xOffset, yOffset, duration=num_seconds)

# time.sleep(7200)

time.sleep(40)
pyautogui.click(xOffset,yOffset,button="left")

for i in range(1):
    pyautogui.press("up")

time.sleep(6)

# pyautogui.click(xOffset,yOffset,button="left")
for i in range(5):
    pyautogui.press("down")