import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rinintha"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE ftds")

print("Database Successfully Created")