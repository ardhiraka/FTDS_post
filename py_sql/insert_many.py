import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rinintha",
  database="ftds"
)

cursor = db.cursor()
sql = "INSERT INTO student (name, address) VALUES (%s, %s)"
values = [
  ("Danu", "Jakarta"),
  ("Fahmi", "Surabaya"),
  ("Sardi", "Bandung"),
  ("Hana", "Depok")
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data added".format(len(values)))