import cx_Oracle

# 单一连接
# connection0=cx_Oracle.connect("orange","orange","10.105.0.229:1521/crmii",encoding="UTF-8")
# cur=connection0.cursor()
# query1=cur.execute('select 1 from dual')
# print(query1.fetchone())
# cur.close()
# connection0.close()

# 连接池
dsn_tns = cx_Oracle.makedsn('10.105.0.229', '1521', service_name='crmii')
pool = cx_Oracle.SessionPool(user='orange', password='orange', dsn=dsn_tns, min=2, max=5, increment=1,encoding='UTF-8')

def GET_CONNECTION():
    # 获取连接
    connection = pool.acquire()
    return connection

def CLS_CONNECTION(connection):
    connection.close()

def CLS_CURSOR(cursor):
    cursor.close()

def GET_CURSOR(connection):
    # 创建游标
    cursor = connection.cursor()
    return cursor

def SQL_QUERY(sql="select 1 from dual",rows=50):
    # try
    try:
        connection = pool.acquire()
        cursor = connection.cursor()

        # 执行SQL查询
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchmany(50)
        # 打印结果
        print(result)
    # 异常处理    
    except cx_Oracle.DatabaseError as e:
        # 打印异常
        print("Fled to execute query: {}".format(e))
        connection.rollback()
    # else
    else:
        connection.commit()
    # finally
    finally:
        # 关闭游标和连接
        cursor.close()
        connection.close()

sql = "select * from crmii.tjjr"
SQL_QUERY(sql,1)