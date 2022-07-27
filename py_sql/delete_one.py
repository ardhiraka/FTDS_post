import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rinintha",
  database="ftds"
)

cursor = db.cursor()
sql = "DELETE FROM student WHERE student_id=%s"
val = (1, )
cursor.execute(sql, val)

db.commit()

print("{} data deleted".format(cursor.rowcount))