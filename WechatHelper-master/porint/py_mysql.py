import  pymysql

#conn=pymysql.connect(host='127.0.0.1', user='root', password='root', database='world', port=3306, charset='utf8')
conn = pymysql.connect(host = '127.0.0.1',user= 'root' ,password='root' ,database='world' ,port = 3306,charset='utf8')
cur = conn.cursor()
select = "select * from  city "
cur.execute(select)
all_data =cur.fetchall()
print(all_data)
conn.close()
