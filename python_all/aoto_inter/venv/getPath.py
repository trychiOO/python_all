import os
def get_basepath():
    #获取文件路径
    basepath = os.path.split(os.path.realpath(__file__))[0]
    return basepath

