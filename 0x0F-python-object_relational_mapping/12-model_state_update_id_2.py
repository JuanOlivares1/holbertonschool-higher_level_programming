#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
               sys.argv[1], sys.argv[2], 'localhost', 3306, sys.argv[3]))

    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
