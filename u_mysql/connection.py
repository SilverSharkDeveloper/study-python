#python -m pip install PyMySQL ->mysql 연결 드라이버
#pip install cryptography ->

import pymysql
import pymysql.cursors

conn = pymysql.connect(host='127.0.0.1',user='root',password='1234',db='app',charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)


# cursor.execute("INSERT INTO app.tbl_member(member_id, member_password, member_name)VALUES('hes1234', '1234', '123')")
# conn.commit()

cursor.execute("select id,member_id,member_password,member_name from tbl_member")
rows = cursor.fetchall()
print(rows)

cursor.close()
conn.close()