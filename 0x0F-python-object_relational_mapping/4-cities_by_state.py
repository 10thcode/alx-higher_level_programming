#!/usr/bin/python3
'''
a script that lists all cities from the database hbtn_0e_4_usa
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
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states \
            ON cities.state_id = states.id"
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)
