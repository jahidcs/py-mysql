import mysql.connector

med_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "db"
)

med_cursor = med_db.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Don", "Ban 21")
med_cursor.execute(sql, val)

med_db.commit()

print(med_cursor.rowcount, "record inserted.")
