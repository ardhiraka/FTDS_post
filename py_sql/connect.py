import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rinintha"
)

if db.is_connected():
  print("Successfully connected to MySQL database")