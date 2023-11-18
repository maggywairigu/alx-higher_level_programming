#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py
<mysql username> <mysql password> <database name> <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute
    ("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state))
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()
