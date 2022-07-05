import mysql.connector

med_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "db"
)

med_cursor = med_db.cursor()

sql = "UPDATE customers SET address='Dhaka' WHERE address='Ban 21'"
med_cursor.execute(sql)
med_db.commit()
print(med_cursor.rowcount, "record(s) affected")
