#!/usr/bin/python3
'''
A script that prints all City objects from the database hbtn_0e_14_usa
'''
from model_city import City
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
    result = session.query(City).join(State).order_by(City.id).all()

    for row in result:
        print("{}: ({}) {}".format(row.states.name,
                                   row.id, row.name))
