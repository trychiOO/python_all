import os
def get_basepath():
    #��ȡ�ļ�·��
    basepath = os.path.split(os.path.realpath(__file__))[0]
    return basepath

