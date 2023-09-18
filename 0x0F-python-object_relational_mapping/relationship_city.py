#!/usr/bin/python3
'''
a script that defines a class City
'''
from relationship_state import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class City(Base):
    '''
    a database model for cities table
    '''
    __tablename__ = 'cities'
    id = Column(
            Integer(),
            primary_key=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
