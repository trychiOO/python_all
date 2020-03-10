# _*_ coding:utf-8 _*_
# author:yr
import os
def combine(save_path):
    p_arr = []
    for root, dirs, files in os.walk(save_path):
        for name in files:
            if name.endswith('.pcm'):
                p_arr.append(os.path.join(root, name))
    print(files)

    f2 = open(save_path +'/' +'all.pcm', 'ab')

    p_arr.sort()

    for i in range(len(p_arr)):
        print(i)

        with open(save_path+'/'+str(i)+'.pcm', 'rb')as f1:
            f2.write(f1.read())

    f2.close()


if __name__ == '__main__':
    combine(r'F:\Youku Files\file')