import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rinintha",
  database="ftds"
)

cursor = db.cursor()
sql = "INSERT INTO student (name, address) VALUES (%s, %s)"
val = ("Raka", "Semarang")
cursor.execute(sql, val)

db.commit()

print("{} succesfully added ".format(cursor.rowcount))