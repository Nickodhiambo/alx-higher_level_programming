#!/usr/bin/python3
"""This script connects a python script to a db using SQLAlchemy ORM"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True
            )

    this_session_maker = sessionmaker(bind=engine)
    this_session = this_session_maker()

    for state, city in this_session.query(State, City).filter(
            State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    this_session.close()
