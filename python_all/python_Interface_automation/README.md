# python_Interface_automation
python接口自动化案例 单接口


common 存放 公共组件 ：

        configDB  链接数据库基类
        configEmail  发送邮件基类
        configHttp   发送post，get请求基类
        Log          日志基类
        HTMLTestRunner 生成网页测试报告基类

config  存放 配置文件：
        
        [DATABASE]
          host 数据库链接地址
          port 数据库链接端口
          username 链接用户名
          password 连接密码
          database 数据库类型
          
       [HTTP]
          scheme 发送请求
          baseurl 接口地址
          port 接口端口
          timeout 超时时间

      [EMAIL]
          on_off 邮件发送开关
          mail_host 邮件的smtp  例如：smtp.qq.com
          mail_user 邮件的用户名
          
          
          
          
          
          
          
          
          mail_pass 邮件的授权码
          mail_port 邮件的端口  一般都是默认25
          
          sender 发送人
          receiver 收件人  如果有多个 可以用 / 隔开
          subject 邮件标题
          content 邮件正文
          testuser = Someone

read 存放读取config 文件 还有 excel 表格类：
      readConfig  读取配置文件类
      readExcel   读取excel表格类

result 存放测试报告类

test_case 存放测试用例类

test_file 存放测试所需的文件：
      case 存放excel 表格
      caselist 配置要执行的 测试用例

getPath 获取目录路径

runAll 执行所有测试用例
