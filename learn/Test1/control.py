#_*_ coding:utf-8 _*_
#author:yr
# ! /usr/bin/env python
# coding=utf-8

import time

from ctypes import windll
#
WM_APPCOMMAND = 0x319
#
APPCOMMAND_VOLUME_UP = 0x0a
#
APPCOMMAND_VOLUME_DOWN = 0x09

APPCOMMAND_VOLUME_MUTE = 0x08  #静音

hwnd=windll.user32.GetForegroundWindow()
       #获取一个前台窗口的句柄

time.sleep(7200)

for  i in range (2):
    windll.user32.PostMessageA(hwnd,WM_APPCOMMAND,0,APPCOMMAND_VOLUME_UP*0x10000)

time.sleep(10800)
for  i in range (2):
    windll.user32.PostMessageA(hwnd,WM_APPCOMMAND,0,APPCOMMAND_VOLUME_DOWN*0x10000)
