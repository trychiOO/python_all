# coding=utf-8
'''
爬取网易云音乐榜单
'''
# 导入需要使用的模块
import os
import csv
import time
import random
import requests
# import multiprocessing
import threading
from lxml import etree
from selenium import webdriver

agents = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
]


class WangyiMusc(object):

    # id表示你要获取排行榜
    # mating是榜单名称
    # url为排行榜页面
    # music_url为歌曲下载页面
    def __init__(self, mating, id):
        self.browser = webdriver.Chrome()
        self.id = id
        self.url = "https://music.163.com/#/discover/toplist?id={0}".format(self.id)
        self.music_url = "http://music.163.com/song/media/outer/url?id={0}.mp3"
        self.mat = mating

    # 由于页面的歌曲信息都存放在页面的ifram里面，所以使用Selenium进入子页面获得代码然后返回
    def get_html(self):
        self.browser.get(self.url)
       # self.browser.switch_to_frame('contentFrame')
        iframe = self.browser.page_source
        time.sleep(5)
        return iframe

    # 使用xpath解析页面的信息进行返回
    def parse_html(self):
        iframe = self.get_html()
        html = etree.HTML(iframe)
        contents = html.xpath('//tbody/tr')

        try:
            for content in contents:
                name = content.xpath('./td/div/div/div/span/a/b/@title')[0].replace(' ', '')
                music_id = content.xpath('./td/div/div/span/@data-res-id')[0].strip()
                # 将歌曲的名称与id传给write_music方法进行下载
                self.write_music(name, music_id)
                num = content.xpath('./td/div/span[@class="num"]/text()')[0].strip()
                date = content.xpath('./td[@class=" s-fc3"]/span/text()')[0].strip()
                singer = content.xpath('./td/div[@class="text"]/@title')[0].strip()
                # 将歌曲的信息构建成个元组类型
                items = num, name, date, singer

                # 每获得一次歌曲信息后返回一次
                yield list(items)

        except Exception as e:
            print('解析失败！', e.args)

    # 获取到目前的日期
    def get_date(self):
        t = time.localtime()
        tt = time.strftime('%Y年%m月%d日', t)
        return tt

    # 得到歌曲的名称与id,这里进行下载
    def write_music(self, name, music_id):
        url = self.music_url.format(music_id)
        agent = random.choice(agents)
        try:
            headers = {
                'User-Agent': agent
            }
            music = requests.get(url, headers=headers)

            if music.status_code == 200:
                # 把歌曲保存到目前日期下的榜单名称下面,方便查看
                path = self.get_date() + os.sep + self.mat + os.sep
                # 查询是否有这个地址,如果没有递归创建
                if not os.path.exists(path):
                    os.makedirs(path)
                with open(path + name + '.mp3', 'ab') as f:
                    f.write(music.content)
                    print('下载 ' + name + " 成功...")

        except Exception as e:
            print("下载 {0} 失败!!!".format(name), e.args)

    # 保存榜单的信息
    def write_items(self):
        # 将信息保存至目前日期的下面,方便查找
        path = self.get_date() + os.sep + self.mat
        try:
            # 判断是否有这个文件，如果没有者创建
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path + '榜单信息.csv', 'w', encoding='utf-8') as file:
                # 使用cvs格式进行保存
                csvfile = csv.writer(file)
                csvfile.writerow(['排名', '歌名', '时长', '歌手'])
                for parse in self.parse_html():
                    csvfile.writerow(parse)
                print("存储信息成功.")
        except Exception as e:
            print("存储信息失败!", e.args)


def operation(mating, id):
    try:
        # 实例化对象
        music = WangyiMusc(mating, id)
        # 获取要爬取的页面的HTML文件
        music.get_html()
        # 解析页面，将需要的信息进行返回,并开始下载歌曲
        music.parse_html()
        # 获取目前的日期
        music.get_date()
        # 保存需要的信息
        music.write_items()
        print("下载完成...")
        # 关闭browser
        music.browser.close()
    except Exception as e:
        print("下载失败!", e.args)


# 选择的界面
def user_select():
    # 每个榜单的id
    ids = ['19723756', '3779629', '2884035', '3778678', '991319590',
           '2408901803', '1978921795', '71385702', '2462790889',
           '10520166', '3812895', '60131', '71384707', '180106', '60198',
           '27135204', '11641012', '120001', '2323534945', '745956260',
           '2023401535', '2006508653', '21845217', '112463',
           '112504', '64016', '10169002', '1899724']

    # 每个榜单的名称
    names = ['云音乐飙升榜', '云音乐新歌榜', '网易原创歌曲榜',
             '云音乐热歌榜', '江小白YOLO云音乐说唱榜', '公告牌音乐榜', '云音乐电音榜',
             '云音乐电音榜', '云音乐ACG音乐榜', 'YY音乐榜', '云音乐国电榜', '云音乐国电榜',
             '云音乐国电榜', '云音乐古典音乐榜', 'UK排行榜周榜', '美国Billboard周榜',
             '法国 NRJVos Hits 周榜', 'iTunes榜', 'Hit FMTop榜', '说唱TOP榜', '云音乐韩语榜',
             '英国Q杂志中文版周榜', '电竞音乐榜', 'KTV唛榜', '台湾Hito排行榜', '中国TOP排行榜（港台榜）',
             '中国TOP排行榜（内地榜）', '香港r台中文歌曲龙虎榜', '中国嘻哈榜']
    musics = {}
    nums = {}

    # 将名称与id存放在musics字典当中
    for mat in range(len(ids)):
        musics[names[mat]] = ids[mat]

    # 给每一个榜单设置一个编号
    for num in range(1, len(names) + 1):
        nums[num] = names[num - 1]

    # 输入编号与榜单名称,便于查看
    for k, v in nums.items():
        print(k, ":", v)

    # 将榜单与id打包以元组的方式放入列表当中
    music_list = list(musics.items())

    # 因为使用4个线程，所以构建一个列表
    list1 = [i for i in range(len(music_list)) if i % 4 == 0]

    # 选择要下载的榜单
    n = int(input('请输入你要下载的榜单(请输入数字,输入0全部提取):'))

    # 如果需要全部下载,使用多线程
    if n == 0:
        for t in list1:
            t1 = threading.Thread(target=operation, args=music_list[t])
            t2 = threading.Thread(target=operation, args=music_list[t + 1])
            t3 = threading.Thread(target=operation, args=music_list[t + 2])
            t4 = threading.Thread(target=operation, args=music_list[t + 3])

            t1.start()
            t2.start()
            t3.start()
            t4.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()

    # 如果只是下载某个榜单,者传入榜单名称与id
    id = musics[nums[n]]
    mating = nums[n]

    operation(mating, id)


if __name__ == '__main__':
    # 程序开始
    user_select()
