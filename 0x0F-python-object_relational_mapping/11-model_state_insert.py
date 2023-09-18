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

    my_session_maker = sessionmaker(bind=engine)
    my_session = my_session_maker()

    Base.metadata.create_all(engine)

    new_state = State(name="Louisiana")
    my_session.add(new_state)
    my_session.commit()
    print(new_state.id)
    my_session.close()
