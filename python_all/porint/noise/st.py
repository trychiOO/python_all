# -*- coding: utf-8 -*-
import pythoncom
from win32com import client

pythoncom.CoInitialize()
engine = client.Dispatch("SAPI.SpVoice")
engine.Speak('Hello world')

import pyttsx3

# 初始化， 必须要有
engine = pyttsx3.init()

engine.say('Hello')
engine.say('我会说中文了，开森，开森')
# 注意，没有本句话是没有声音的
engine.runAndWait()

engine.say('我能说第二句话了')
engine.runAndWait()