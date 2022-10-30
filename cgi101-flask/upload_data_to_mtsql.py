# 連接資料庫
import pymysql

host = 'localhost'
port = 3306
user = 'root'
passwd = 'root'
db = 'TESTDB'
charset = 'utf8mb4'

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
print('Successfully connected!')

cursor = conn.cursor()

import json
import time

path = 'Staff.json'
with open(path, 'r', encoding='utf-8') as f:
    jsondata = json.loads(f.read())

jsondata

sql_insert = """
INSERT INTO Staff (ID, Name, DeptId, Age, Gender, Salary, recordDt)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""

import time
t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
values = [tuple(jsondata[d].values()) + (t,) for d in jsondata]
values

# 將 SQL 批量執行
print('新增資料筆數:', cursor.executemany(sql_insert, values))

# Commit 並檢查資料是否存入資料庫
conn.commit()

# 關閉連線
cursor.close()
conn.close()