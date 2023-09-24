#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username, mysql password, and database name
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
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

        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
        for state in states_with_a:
            print(f"{state.id}: {state.name}")

        session.close()
