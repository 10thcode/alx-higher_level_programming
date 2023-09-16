#!/usr/bin/python3
'''
a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
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
    cursor.execute(
            "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id"
    )
    result = cursor.fetchall()

    for row in result:
        print(row)
