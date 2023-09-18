#!/usr/bin/python3
'''
a script that changes the name of a State object from
the database hbtn_0e_6_usa
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
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.add(state)
    session.commit()
