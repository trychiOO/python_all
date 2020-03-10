all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
all(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
all([0, 1,2, 3])          # 列表list，存在一个为0的元素
all(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
#print (all(()))  # 元组tuple，存在一个为0的元素
all([])  # 空列表，返回true
print(all(()))# 空元组，返回truehar
print(chr(2155))