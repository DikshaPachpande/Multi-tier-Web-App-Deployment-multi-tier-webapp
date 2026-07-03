import pymysql

connection=pymysql.connect(
host="YOUR-RDS-ENDPOINT",
user="admin",
password="Password123",
database="company"
)
