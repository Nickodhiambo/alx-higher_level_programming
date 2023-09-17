#!/usr/bin/python3
"""This script uses SQLAlchemy to map a python script to database"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True
            )

    session_maker = sessionmaker(bind=engine)
    _session = session_maker()

    for state in _session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    _session.close()
