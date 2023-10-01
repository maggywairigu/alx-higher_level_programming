#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
Your script should take 3 arguments:
mysql username, mysql password, and database name
You must use the module SQLAlchemy
You must import State and Base from model_state
Your script should connect to a MySQL server running on localhost at port 3306
The state you display must be the first in states.id
The results must be displayed as they are in the example below
If the table states is empty, print Nothing followed by a new line
Your code should not be executed when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
