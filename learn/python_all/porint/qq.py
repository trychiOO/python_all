#动态
#0加载了4页信息，60加载了3、4页的信息
import csv
import requests
import json

fp = open("F:/QQ音乐_0.csv",'wt',newline='',encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(['歌曲','歌手','时间'])

#因为第一个页面就加载了所有的信息，就不需要翻页了，要不然会重复
urls = ["https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?tpl=3&page=detail&date=2019-03-01&topid=4&type=top&song_begin={}".format(i) for i in range(0,1)]
for url in urls:
    print(url)
    r = requests.get(url)
    results = json.loads(str(r.text))
    fins = results.get("songlist")
    for fin in fins:
        names = fin.get("data").get("singer")
        #向获取到这里，这是一个列表，不能再用get，需要转换一下格式
        author = names[0].get("name")#歌手
        songnames = fin.get("data").get("songname")#歌手
        times = fin.get("data").get("interval")#时间
        #网页数据中给的时间是以s为单位我们要转换为分
        time = str(int(times)//60) + ':'+str(int(times)%60)
        writer.writerow([songnames,author,time])

fp.close()


