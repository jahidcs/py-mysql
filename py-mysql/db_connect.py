import mysql.connector

med_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "db"
)

med_cursor = med_db.cursor()

# med_cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
med_cursor.execute("SHOW TABLES")

for tables in med_cursor:
    print(tables)
