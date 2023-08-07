1. 安装必要的库：在Python中，你可以使用`pandas`库来获取数据，使用`cx_Oracle`库来连接和插入数据到Oracle数据库。你可以使用以下命令来安装这些库：

```python
pip install pandas
pip install cx_Oracle
```

2. 导入必要的库：

```python
import pandas as pd
import cx_Oracle
```

3. 连接到Oracle数据库：

```python
# 替换以下信息为你自己的数据库连接信息
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
conn = cx_Oracle.connect(user='your_username', password='your_password', dsn=dsn_tns)
```

4. 获取上海交易所的成交金额数据：

```python
# 使用pandas的read_html函数获取网页中的表格数据
url = 'http://www.sse.com.cn/market/sseindex/indexlist/s/i000001/desc.dot'
tables = pd.read_html(url)

# 获取指定表格的数据
df = tables[1]  # 假设成交金额数据在第二个表格中，根据实际情况调整索引

# 可以根据需要对数据进行处理，例如删除不需要的列、重命名列名等
df = df[['日期', '成交金额(亿元)']]  # 只保留日期和成交金额两列
df.columns = ['date', 'amount']  # 重命名列名
```

5. 将数据插入到Oracle数据库中：

```python
# 将数据插入数据库中的表
cursor = conn.cursor()
for index, row in df.iterrows():
    cursor.execute("INSERT INTO your_table_name (date_column, amount_column) VALUES (:1, :2)",
                   (row['date'], row['amount']))
conn.commit()
cursor.close()
```

注意：
- 在上述代码中，需要将以下部分替换为你自己的信息：
  - 数据库连接信息（主机名、端口号、服务名、用户名、密码）
  - 数据库中的表名、列名
- 请确保你的网络能够访问上海证券交易所的网站。