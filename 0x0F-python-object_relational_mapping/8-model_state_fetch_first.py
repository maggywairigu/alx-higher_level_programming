#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username, mysql password, and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
The state you display must be the first in states.id
You are not allowed to fetch all states from the database before displaying the result
The results must be displayed as they are in the example below
If the table states is empty, print Nothing followed by a new line
Your code should not be executed when imported
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python list.py <username> <pswd> <db>")
        sys.exit(1)

        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

        Session = sessionmaker(bind=engine)
        session = Session()

        first_state = session.query(State).order_by(State.id).first()

        if first_state:
            print(f"{first_name.id}: {first_state.name}")
        else:
            print("Nothing")

        session.close()
