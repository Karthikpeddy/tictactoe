import mysql.connector
import pandas as pd
data=pd.read_csv("C:\\Users\\Eigennet LLC\\Desktop\\db.csv",delimiter=",")
# "C:\Users\Eigennet LLC\Desktop\db.csv"
conn=mysql.connector.connect(username="root",password="12345",host="localhost",db="tutorial1")
if conn.is_connected():
    print("the connection is established")
# sql_quer = "create table abhi(name varchar(20));"
sql_quer="ALTER TABLE abhi ADD column salary integer(10);"
cur = conn.cursor()
list_csv=[]
list_csv=[list(row) for row in data.values]
for i in list_csv:
    sql=f"INSERT INTO abhi (name, salary) VALUES({i})"
    print("tha values are added")
# for i in data:
#     print(i)

#     cur.execute(sql)
#     print("tables updated")
# cur.execute(sql_quer)
conn.close()