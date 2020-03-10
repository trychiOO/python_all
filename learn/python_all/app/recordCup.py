# /usr/bin/python
# encoding:utf-8
import csv
import os
import time


# 控制类
class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.alldata = [("timestamp", "cpustatus")]

    # 单次测试过程
    def testprocess(self):
        result = os.popen("adb shell top  -n 1  | findstr com.huawei.heal+")
        # 运行命令得到： 30464 u0_a129  10 -10  22% S    44 1823308K 158792K  fg ...
        for line in result.readlines():
            cpuvalue = line.split("%")[0]  # 30464 u0_a129  10 -10  24 for line in result.readlines():
            result1 = line.split("%")[0]  # 得到   30464 u0_a129  10 -10  24
            result2 = result1.split(" ")  # 根据空格隔开
            cpuvalue = result2[len(result2) - 1]  # 获取数组最后一个，即为cpu%
            currenttime = self.getCurrentTime()
            self.alldata.append((currenttime, cpuvalue))


    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(3)

    # 获取当前的时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # 数据的存储
    def SaveDataToCSV(self):
        csvfile = open('cpustatus.csv', 'w')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCSV()
