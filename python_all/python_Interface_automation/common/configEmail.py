import os
import smtplib
import threading
import zipfile
import glob
import getPath
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from read import readConfig

localReadConfig = readConfig.ReadConfig()
#SMTP 服务器主机
mail_host = localReadConfig.get_email('mail_host')
#指定 SMTP 服务使用的端口号
mail_port = localReadConfig.get_email('mail_port')
#用户名
mail_user = localReadConfig.get_email('mail_user')
#邮件密码  授权码
mail_pass = localReadConfig.get_email('mail_pass')
#邮件发送方邮箱地址
sender = localReadConfig.get_email('sender')
#接受邮件放邮箱地址
value = localReadConfig.get_email('receiver')
title = localReadConfig.get_email('subject')
content = localReadConfig.get_email('content')

class Email():
    def __init__(self):
        self.receiver = []
        #获取接收人 列表
        for r in str(value).split('/'):
            self.receiver.append(r)
        #格式化时间
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.subject = title+" "+data
        self.msg = MIMEMultipart('mixed')

    def config_header(self):
        #设置邮件发送头
        self.msg['Subject'] = self.subject
        self.msg['From'] = sender
        self.msg['To'] = ":".join(self.receiver)

    def config_content(self):
        #设置邮件主题
        content_plain = MIMEText(content,'plain')
        self.msg.attach(content_plain)

    def config_file(self):
        #如果有文件，就配置邮件附件  filename 用英文形式，如果用中文 需要改动
        if self.check_file():
            htmlpath = os.path.join(getPath.get_basepath(),'result','report.html')
            html = open(htmlpath,'rb').read()
            filehtml = MIMEText(html,'base64','utf-8')
            filehtml['Content-Type'] = 'application/octet-stream'
            filehtml['Content-Disposition'] = 'attachment; filename="test.html"'
            self.msg.attach(filehtml)

    def check_file(self):
        reportpath = os.path.join(getPath.get_basepath(),'result','report.html')
        if os.path.isfile(reportpath) and not os.stat(reportpath) == 0:
            return True
        else:
            return False

    def send_email(self):
        self.config_header()
        self.config_content()
        self.config_file()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(mail_host,mail_port)
            smtp.login(mail_user, mail_pass)
            smtp.sendmail(sender, self.receiver, self.msg.as_string())
            smtp.quit()
            print('邮件已发送注意查收')
        except Exception as ex:
            print('邮件发送失败，错误详情：'+str(ex))
