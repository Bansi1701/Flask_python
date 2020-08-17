# first install pymysql : pip install pymysql
# sqlyog

from flask import Flask
import pymysql

app = Flask ( __name__ )

@app.route ( '/' )
def insertLogin():
    # connection is object of pymysql connection
    connection = pymysql.connect (host='localhost', user='root', password='root', db='pythondb', port=3306)
    # arguments are details of database (sqlyog)
    un = "admin1"
    pwd = "admin1"

    cursor1 = connection.cursor()  # cursor is pointer of database
    cursor1.execute ("INSERT INTO loginmaster(username,password) VALUES ('{}','{}')".format('un','pwd'))
    # loginmaster = table name
    # username,password = column name
    connection.commit()

    cursor1.close()
    connection.close()

    return 'insert successfully...'

if __name__ == '__main__':
    app.run(debug=True)
