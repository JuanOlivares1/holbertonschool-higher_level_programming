#!/usr/bin/python3
"""Script - lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
FROM cities JOIN states ON state_id = states.id \
ORDER BY cities.id ASC")
    for data in cursor.fetchall():
        print(data)
    cursor.close()
    db.close()
