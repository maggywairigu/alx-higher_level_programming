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

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to a database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c`\
    INNER JOIN `states` as `s`\
    ON `c`.`state_id` = `s`.`id`\
    ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
