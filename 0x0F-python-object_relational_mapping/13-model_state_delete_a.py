#!/usr/bin/python3
"""This script connects a python script to a db using SQLAlchemy ORM"""

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

    this_session_maker = sessionmaker(bind=engine)
    this_session = this_session_maker()

    states = this_session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        this_session.delete(state)
    this_session.commit()
    this_session.close()
