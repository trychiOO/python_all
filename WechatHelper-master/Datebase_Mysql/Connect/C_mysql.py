# # -*- coding:utf8 -*-
#
from pymysql import connect

# #基本信息   host  172.0.0.1 port 3306   user password  database
try:
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='music',
        charset='utf8')
    cursor = conn.cursor()
except Exception as e:
    print(e)
else:
    # print("Connect success" % cursor)
    print('Connect Success:%s' % cursor)


# 查询：
def execute_sql(command, sql):
    """
    查询数据库
    :param command:
    :param sql:
    :return:
    """
    if command in ('select', 'SELECT'):
        sql = sql.encode('utf-8')
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            conn.close()
    elif command in ('updata', 'delete', 'insert'):
        # 如果是 删 增 更新
        sql = sql.encode('utf8')
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            conn.close()
    else:
        print("command error")


if __name__ == '__main__':
    sel_sql = "select * from singer where id = '39521' "
    print(execute_sql('select', sel_sql))
