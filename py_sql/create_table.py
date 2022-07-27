import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rinintha",
  database="ftds"
)

cursor = db.cursor()
sql = """CREATE TABLE student (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
cursor.execute(sql)

print("Student Table Successfully Created")