#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql://{}:{}@{}:{}/{}'.format(
               sys.argv[1], sys.argv[2], 'localhost', 3306, sys.argv[3]))

    new_state = State(name='Louisiana')

    Base.metadata.create_all(engine)
    session = sessionmaker(engine)()
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
