import mysql.connector

med_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "db"
)

med_cursor = med_db.cursor()

sql = "DELETE FROM customers WHERE address = 'Dhaka'"

med_cursor.execute(sql)
med_db.commit()
print(med_cursor.rowcount, "record(s) deleted")
