import pandas as pd
import cx_Oracle
import os

# 当前路径
cur_path = os.path.abspath(os.path.dirname(__file__))
print(cur_path)

# 连接数据库，获取游标
con = cx_Oracle.connect('orange/orange@10.105.0.229:1521/crmii')

# 操作sql语句，将需要导出的数据表名称放在txt文档中，遍历读取每一行获取表格名称
with open(os.path.join(cur_path, "csv", "数据表名称.txt"), "r") as f:
    for line in f.readlines():
        table = line.strip()
        # 跳过空白行
        if not table:
            continue
        print(table)
        try:
            # 使用pandas的read_sql_query函数直接读取到DataFrame
            df = pd.read_sql_query(f"SELECT * FROM {table}", con)

            # 导出为Excel文件
            df.to_excel(os.path.join(cur_path, "csv", f"{table}.xlsx"), index=False)
        except Exception as e:
            print(f"导出失败数据表为{table}，失败原因为", e)

# 关闭链接
con.close()