# -*- coding:utf-8 -*-
#文件批处理重命名程序

import os, sys

def rename():
    # 输入重命名的相关参数
    path = input("请输入文件夹路径(直接复制路径粘贴)：")
    name = input("请输入文件重命名的名称(比如picture)：")
    startNumber = input("请输入文件重命名开始的编号：")
    fileType = input("请输入文件后缀名(比如.jpg,.mp4,.txt等)：")
    print("正在以" + name + startNumber + fileType + "批量重命名文件")

    count = 0
    # 将文件夹中的文件名打开为一个列表
    fileList = os.listdir(path)
    # 循环取出每一个文件名，进行重命名
    for file in fileList:
        # 原始图片的路径
        old_name = os.path.join(path, file)
        if os.path.isdir(old_name):
            continue
        # 修改后图片的路径
        new_name = os.path.join(path, name + str(count + int(startNumber)) + fileType)
        # 修改图片路径，也就是图片重命名
        os.rename(old_name, new_name)
        count += 1
    print("一共重命名了" + str(count) + "个文件")

if __name__ == '__main__':
    rename()
