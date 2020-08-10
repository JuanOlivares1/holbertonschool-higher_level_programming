#!/usr/bin/python3
"""Script - lists all states from the database hbtn_0e_0_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":

    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
               sys.argv[1], sys.argv[2], 'localhost', 3306, sys.argv[3]))

    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()

    table = session.query(City, State).filter(City.state_id == State.id)\
                                      .order_by(City.id.asc()).all()

    for ctiy, state in table:
        print("{}: ({}) {}".format(state.name, ctiy.id, ctiy.name))
