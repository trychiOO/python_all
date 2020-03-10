#-*- coding:utf8 -*-
import requests
import urllib3
"""用 栈  对比"""
class Slution:
    def removeDuplicates(self, S: str) -> str:
        stack = []  # 定义一个栈
        for i in S:
            if not stack:  # 如果当前栈为空
                stack.append(i)
            elif stack[-1] == i:  # 如果当前元素与栈顶元素相等
                stack.pop()
            else:
                stack.append(i)

        return ''.join(stack)


def get_news():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    #print(r.json())
    contents = r.json()['content']
    #print(contents)
    translation = r.json()['translation']
    return contents,translation

my_friend =get_news()
print(my_friend)