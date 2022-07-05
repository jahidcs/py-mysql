import mysql.connector

med_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password"
)

med_cursor = med_db.cursor()
med_cursor.execute("SHOW DATABASES")

for db in med_cursor:
    print(db)
    