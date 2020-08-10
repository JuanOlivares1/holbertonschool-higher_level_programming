#!/usr/bin/python3
"""Lists all State objects that contain the letter
 a from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
               sys.argv[1], sys.argv[2], 'localhost', 3306, sys.argv[3]))

    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    table = session.query(State).filter(State.name.contains('a'))

    for state in table:
        print("{}: {}".format(state.id, state.name))

    session.close()
