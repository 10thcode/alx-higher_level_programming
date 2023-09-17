#!/usr/bin/python3
'''
defines a class State
'''
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


Base = declarative_base()


class State(Base):
    '''
    a database model for states table
    '''
    __tablename__ = 'states'
    id = Column(
            Integer(),
            primary_key=True,
            autoincrement=True,
            unique=True,
            nullable=False
    )
    name = Column(String(128), nullable=False)
