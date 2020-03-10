import subprocess
import re

os.system('adb version')
os.system('adb devices')  # os.system是不支持读取操作的
out = os.popen('adb shell "dumpsys activity | grep "mFocusedActivity""').read()  # os.popen支持读取操作
print(out)


# 下面的代码是获取当前窗口的component参数
def getFocusedPackageAndActivity():
    pattern = re.compile(
        r"[a-zA-Z0-9\.]+/[a-zA-Z0-9\.]+")

    out = os.popen("adb shell dumpsys window windows | findstr \/ | findstr name=").read()  # window下使用findstr
    list = pattern.findall(out)
    component = list[0]

    return component


print(getFocusedPackageAndActivity())