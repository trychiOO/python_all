import time
import os
import numpy as np
import subprocess
#import pyaudio
import wave
# def play(filename):
#     chunk = 1  # 指定WAV文件的大小
#     wf = wave.open(filename, 'rb')
#     p = pyaudio.PyAudio()  # 初始化PyAudio模块
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
#                     rate=wf.getframerate(), output=True)
#     data = wf.readframes(chunk)  # 读取第一帧数据
#
#     while data != b'':
#         stream.write(data)  # 将帧写入数据流对象中，以此播放
#         data = wf.readframes(chunk)  # 继续读取后面的帧
#     stream.stop_stream()  # 停止数据流
#     stream.close()  # 关闭数据流
#     p.terminate()  # 关闭 PyAudio


def huawei_xiaonangua_rec():
   # path = r"Z:\数据标注\xdxd\waitcheck\test"
    for root, dirs, files in os.walk(path):
        for name in files:
            print(name)
            #stop process
            os.system(r"adb shell rm /mnt/*.pcm")
            cmd = 'adb shell "ps -ef | grep SampleApp | awk \'{print $2}\' | xargs kill"'
            p3 = subprocess.Popen(cmd)
            p3.wait()
            cmd2 = 'adb shell "ps -ef | grep sample_ai_i2s0 | awk \'{print $2}\' | xargs kill"'
            p4 = subprocess.Popen(cmd2)
            p4.wait()

            #recording
            p1 = subprocess.Popen(
                r"adb shell cd /mnt/&& sample_ai_i2s0 500 /mnt/sdcard/test.pcm")
            time.sleep(2)
            p2 = subprocess.Popen(
                r"adb shell cd /mnt/&&/data/voiceAsst/bin/SampleApp")
            play(root + "/" + name)
            time.sleep(0.5)

            # stop process
            cmd = 'adb shell "ps -ef | grep SampleApp | awk \'{print $2}\' | xargs kill"'
            p3 = subprocess.Popen(cmd)
            p3.wait()
            cmd2 = 'adb shell "ps -ef | grep sample_ai_i2s0 | awk \'{print $2}\' | xargs kill"'
            p4 = subprocess.Popen(cmd2)
            p4.wait()

            os.system(r"adb pull /mnt/audio_send_before_channel.pcm C:\Users\soundai\Desktop\rec\%s.pcm"% name[:-4])
            time.sleep(10)

            os.remove(root + "/" + name)



if __name__ == '__main__':
    huawei_xiaonangua_rec()

    # "/data/voiceAsst/bin/SampleApp"
    # "sample_ai_i2s0 500 /mnt/sdcard/test.pcm"


