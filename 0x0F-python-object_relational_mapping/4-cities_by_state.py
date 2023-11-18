#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
Usage: ./4-cities_by_state.py <username> <password> <database>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
