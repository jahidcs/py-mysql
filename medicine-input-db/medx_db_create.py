import mysql.connector

medx_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "medicine_db"
)

med_cursor = medx_db.cursor()

query = '''
    CREATE TABLE medicine (
        ID INT AUTO_INCREMENT PRIMARY KEY,
        name varchar(255),
        generic varchar(255),
        form varchar(255),
        strength varchar(255),
        pharma varchar(255),
        price varchar(255)
    )
'''

med_cursor.execute(query)
