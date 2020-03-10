#coding: utf-8
import smtplib
from email.mime.text import MIMEText             # 文本
from email.mime.multipart import MIMEMultipart   #附件
from email.mime.image import MIMEImage           #图片


import time
import datetime
smtp_host = 'smtp.qq.com'
smtp_port = 465
user = '1162551619@qq.com'
password = 'vfhpxdbvouuafhdi'
fromMail= '1162551619@qq.com'
toMail=  '1162551619@qq.com'
smtp = smtplib.SMTP_SSL(smtp_host,smtp_port)
smtp.login(user,password)
#文本格式：
# msg = MIMEText()
# 发送文本内容
text_info = 'hello world \nhahha\n  hahah\n ehhehehehe\nwww.baidu.com'
#发送URL
url = "https://www.baidu.com"
html_info = """
    <p>点击以下链接，你怎么这么笨呢？</p>
    <p><a href="%s">click me</a></p>
    <p>i am very glasses for you</p>
    """ % url
text_sub = MIMEText(html_info,'plain', 'utf-8')
text_sub["Content-Disposition"] = 'attachment; filename="baidu.html"'


#发送附件：
msg = MIMEMultipart('mixed')
text_info = '自动化测试报告\n请下载附件后查看，不要直接预览'
text_sub = MIMEText(text_info, 'plain', 'utf-8')
msg.attach(text_sub)
file =open(r'D:\PycharmProjects\WechatHelper-master\easy_au\report\report.html','rb').read()
txt = MIMEText(file, 'base64', 'gbk32')
txt["Content-Type"] = 'application/octet-stream'
#以下代码可以重命名附件
time_ = str(datetime.datetime.now())
txt.add_header('Content-Disposition', 'attachment', filename='自动化测试报告'+time_+'.html')
msg.attach(txt)



msg['From'] = fromMail
msg['TO'] = toMail
time_ = str(datetime.datetime.now())
msg['Subject']='自动化测试报告'+time_




smtp.send_message(from_addr=fromMail,to_addrs=toMail,msg=msg)
smtp.close()







