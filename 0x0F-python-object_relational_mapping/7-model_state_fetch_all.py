#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
        sys.argv[1], sys.argv[2], 'localhost', 3306, sys.argv[3]))

    table = sessionmaker(engine)().query(State).order_by(State.id)

    for state in table:
        print("{}: {}".format(state.id, state.name))
