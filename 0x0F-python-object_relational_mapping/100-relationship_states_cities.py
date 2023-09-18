#!/usr/bin/python3
'''
a script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
'''
from relationship_city import City
from relationship_state import State, Base
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State()
    state.name = "California"
    session.add(state)
    session.commit()

    city = City()
    city.name = "San Francisco"
    city.state_id = state.id
    session.add(city)
    session.commit()
