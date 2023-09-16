#!/usr/bin/python3
'''
A script that lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            user=username,
            password=password,
            database=database,
            host="localhost",
            port=3306
    )
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id')
    result = cursor.fetchall()

    for row in result:
        print(row)
