#!/usr/bin/python3
'''
a script that takes in the name of a state as an argument
and lists all cities of that state.
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
    query = "SELECT cities.name \
            FROM cities \
            WHERE cities.state_id = ( \
            SELECT states.id \
            FROM states \
            WHERE states.name = %s) \
            ORDER BY cities.id"
    cursor.execute(query, (state,))
    result = cursor.fetchall()
    list_view = []

    for row in result:
        list_view.append(row[0])

    print(", ".join(list_view))
