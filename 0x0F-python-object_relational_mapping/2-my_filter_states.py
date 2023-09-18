#!/usr/bin/python3
'''
a script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
'''
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
            user=username,
            password=password,
            database=database,
            host="localhost",
            port=3306
    )

    cursor = db.cursor()
    statement = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id"
    cursor.execute(statement.format(state))
    result = cursor.fetchall()
    for row in result:
        print(row)
