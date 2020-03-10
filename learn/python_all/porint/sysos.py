import os
import time
import shutil
seconds1 = int(input("请输入pull文件的时间："))
# 根据文件的大小和网速来确定时间        建议60s
seconds2 = int(input("请输入下次循环的间隔时间"))
number = int(input("请输入循环次数"))

for i in range(number):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

    os.chdir(r'C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\小爱同学')
    os.mkdir(now)
    path2 = r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\小爱同学" + "\\" + now
    time.sleep(seconds2)
    os.system(r"adb shell rm/sai_save_basex_data")
    os.system(r"adb pull sdcard/original_result.pcm")

    time.sleep(seconds1)

    shutil.move("2019-04-01.log", path2)

    # time.sleep(60)
    os.system(r"adb shell touch sai_save_basex_data")
    time.sleep(120)

    time.sleep(420)

print("日志打印完成")






