import pandas as pd
import cx_Oracle
import os

# 当前路径
cur_path = os.path.abspath(os.path.dirname(__file__))
print(cur_path)

# 连接数据库，获取游标
con = cx_Oracle.connect('orange/orange@10.105.0.229:1521/crmii')
cur = con.cursor()

# 操作sql语句，将需要导出的数据表名称放在txt文档中，遍历读取每一行获取表格名称
with open(cur_path+"\csv\数据表名称.txt","r") as f:
    for line in f.readlines():
        try:
            table = line.strip()
            # 跳过空白行
            if not table:
                continue
            print(table)
            sql = "select * from %s"%(table)
            cur.execute(sql)          # 执行sql查询
        except Exception as e:
            print("导出失败数据表为%s，失败原因为"%(table),e)
            continue

        # 获取查询结果
        rows = cur.fetchall()

        # 获取列名
        columns = [i[0] for i in cur.description]

        # 创建pandas DataFrame
        df = pd.DataFrame(rows, columns=columns)

        # 导出为Excel文件
        df.to_excel(cur_path+"\csv\{}.xlsx".format(table), index=False)


# 关闭游标和链接
cur.close()
con.close()
