
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp = "smtp.qq.com"

sender = '1162551619@qq.com'
receiver = '1162551619@qq.com'
# 授权密码
pwd = 'vfhpxdbvouuafhdi'

title = "Test"
contents = "{}发送给{}的邮件".format(sender, receiver)


try:
    ldqplxo = MIMEText(contents, 'plain', 'utf-8')
    ldqplxo['From'] = Header(sender, 'utf-8')
    ldqplxo['To'] = Header(receiver, 'utf-8')
    ldqplxo['Subject'] = Header(title, 'utf-8')
    # 获取证书：
    mbdrewr = smtplib.SMTP_SSL(smtp, 465)
    print(mbdrewr)
    mbdrewr.login(sender, pwd)
    mbdrewr.sendmail(sender, receiver, ldqplxo.as_string())
    mbdrewr.quit()
except Exception as e:
    print ('错误>>>', e)