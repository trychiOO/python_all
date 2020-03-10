import os

abs_path =  str(os.path.dirname(__file__))
ispath = abs_path.replace("/","//")
img_path =ispath+"//img"
ex_path = ispath+"//query.xlsx"
mkpath = img_path
os.makedirs(mkpath)
