#-*- coding: utf-8 -*-

original_list1=[" "]
original_list2=[" "]
original_list3=[" "]
original_list4=[" "]
newlist1=[" "]
newlist2=[" "]
newlist3=[" "]
newlist4=[" "]
newtxt1=""
newtxt2=""
newtxt3=""
newtxt4=""

#first way to readline
f = open(r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\fh\1\1.txt","r+")       # 返回一个文件对象
line = f.readline()              		 # 调用文件的 readline()方法
while line:
	original_list1.append(line)
	line = f.readline()
f.close()

#use "set()" remove duplicate str in the list
# in this way,list will sort randomly
newlist1 = list(set(original_list1))
#newlist1 = {}.fromkeys(original_list1).keys()  #faster

#rebuild a new txt
newtxt1="".join(newlist1)
f1 = open("noduplicate1.txt","w")
f1.write(newtxt1)
f1.close()

###################################################################

#second way to readline

for line in open(r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\fh\1\1.txt","r+"):
    original_list2.append(line)

newlist2 = list(set(original_list2))
newlist2.sort(key=original_list2.index)     			#sort
#newlist2 = sorted(set(original_list2),key=l1.index)    #other way

newtxt2="".join(newlist2)
f2 = open("noduplicate2.txt","w")
f2.write(newtxt2)
f2.close()
###################################################################

#third way to readline
f3 = open(r"C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\fh\1\1.txt","r")
original_list3 = f3.readlines()      		#读取全部内容 ，并以列表方式返回

for i in original_list3:					#遍历去重
	if not i in newlist3:
        	newlist3.append(i)

newtxt3="".join(newlist3)
f4 = open("noduplicate3.txt","w")
f4.write(newtxt3)
f4.close()


###################################################################

#fourth way
f5 = open(r'C:\Users\龙龙.LAPTOP-54PEQUTO\Desktop\fh\1\1.txt',"r+")
try:
    original_list4 = f5.readlines()
    [newlist4.append(i) for i in original_list4 if not i in newlist4]
    newtxt4="".join(newlist4)
    f6 = open("noduplicate4.txt","w")
    f6.write(newtxt4)
    f6.close()
finally:
    f5.close()
