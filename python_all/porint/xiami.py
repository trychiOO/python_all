import requests
from lxml import etree
url_ = "https://www.xiami.com/artist?spm=a1z1s.2943549.1110925385.4.PnoO3b"

headers_ = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87'
}
page_source = requests.get(url=url_, headers=headers_)

print("响应结果：\n", page_source.text)

model = etree.HTML(page_source.text)
songs_list = model.xpath('//div[@class="info"]/p[1]/strong/a/text()')
songer = model.xpath("//div[@class='info']/p[2]")
print("歌曲个数：{}   歌手个数：{}".format(len(songs_list), len(songer)))
for index, item in enumerate(songs_list):
    # 继续处理一首歌曲有多位演唱者的情况，因为每一位演唱者都在一个a标签里面，我们把多个a标签看成一个list集合处理
    songer_list = songer[index].xpath(".//a/text()")
    # 每一首歌曲的每一位演唱者组成一个list集合，我们利用join方法对list集合的每一项进行拼接，组成一个字符串结果
    dealed_songer = ",".join(songer_list)
    # 最后按格式输出结果
    print("{}、{}\t【{}】".format(index + 1, item, dealed_songer))