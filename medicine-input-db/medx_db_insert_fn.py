import mysql.connector

def insert(name, generic, form , strength, pharma,price):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="medicine_db"
   )
    mycursor = mydb.cursor()

    sql = "insert into medicine (name, generic, form, strength, pharma, price) values(%s, %s,%s , %s, %s, %s)"
    val = (name, generic, form , strength, pharma,price)

    mycursor.execute(sql, val)

    mydb.commit()



def app():
    with open('medx.txt') as f:

        for line in f:
            spl = line.split('|')
            insert(spl[0].strip(),spl[1].strip(),spl[2].strip(),spl[3].strip(),spl[4].strip(),spl[5].strip())
            print(spl[0] + " added")

if __name__ =="__main__":
    app()