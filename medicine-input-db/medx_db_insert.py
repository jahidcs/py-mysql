import mysql.connector

file = open("medx.txt", "r")

med_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "medicine_db"
)

med_cursor = med_db.cursor()

def insert_data(file):
    for x in file:
        y = x.split(' | ')
        for i in range(len(y)):
            query = "INSERT INTO medicine (name, generic, form, strength, pharma, price) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (y[0], y[1], y[2], y[3], y[4], y[5])

            med_cursor.execute(query, val)
            med_db.commit()
            print(med_cursor.rowcount, "record inserted.")

insert_data(file)
