#!/usr/bin/python3
'''
a script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection_string = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database)
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.ilike("%a%")).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
