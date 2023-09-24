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
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python list.py <usrname> <pswd> <db> <state>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        cursor = db.cursor()
        query = "SELECT GROUP_CONCAT( \
        cities.name ORDER BY cities.id ASC SEPARATOR ', ') \
        FROM cities JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s"
        cursor.execute(query, (search,))
        cities = cursor.fetchone()[0]
        print(cities)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
