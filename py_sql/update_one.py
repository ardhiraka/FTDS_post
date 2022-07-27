import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rinintha",
  database="ftds"
)

cursor = db.cursor()
sql = "UPDATE student SET name=%s, address=%s WHERE student_id=%s"
val = ("Rachman", "Lombok", 1)
cursor.execute(sql, val)

db.commit()

print("{} data updated".format(cursor.rowcount))