# -*- coding: utf-8 -*-
from aip import AipSpeech
from pydub import AudioSegment
import time

# input your own APP_ID/API_KEY/SECRET_KEY
APP_ID = '16931791'
API_KEY = 'qU69rrklFQDKTa9PoafplXBw'
SECRET_KEY = 'kP105fNL3DxVIaTYQD6xFuStp0p6qYmy '
str = input("请输入要转成语音的文字： ")
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis(str, 'zh', 1, {'vol': 5, 'per': 4})

if not isinstance(result, dict):
    with open('1.wav', 'wb') as f:
        f.write(result)

# sound = AudioSegment.from_mp3('temp.mp3')
# sound.export(time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".wav", format="wav")
