import mysql.connector
import redis
import json
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="fin2022"
)

# if db.is_connected():
#   print("Berhasil terhubung ke database")


# INSERT data
# cursor = db.cursor()
# sql = "INSERT INTO tbl_hakakses (id_module, id_admin) VALUES (%s, %s)"
# val = ("1", "1")
# cursor.execute(sql, val)

# db.commit()

# print("{} data ditambahkan".format(cursor.rowcount))

q = []
cursor = db.cursor()
sql = "SELECT * FROM tbl_konten ORDER BY id_konten ASC"
cursor.execute(sql)
results = cursor.fetchall()

r = redis.Redis()
for data in results:
 r.set(data[0], json.dumps({"id_konten":data[0],"id_admin":data[1],"isi":data[15]}))
 

 print(data[0])
 print("success")






