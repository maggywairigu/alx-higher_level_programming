#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
Your script should take 4 arguments:
mysql username, mysql password, database name and state name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server
running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to a database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities INNER JOIN states ON citites.state_id = states.id WHERE states.name = %s", [argv[4]])

    rows = cur.fetchall()
    j = []
    for i in rows:
        j.append(i[1])
    print(", ".join(j))

    #clean up process
    cur.close()
    db.close()
