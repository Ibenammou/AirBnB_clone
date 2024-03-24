#!/usr/bin/python3
""" State Module for HBNB project """

import models
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, aliased
from models.base_model import BaseModel
import uuid
from os import getenv
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(String(60), nullable=False, primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(128), nullable=False)

    # for DBStorage
    if models.storage_type == 'db':

        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref="state")

    if models.storage_type != 'db':
        @property
        def cities(self):
            """ Getter attribute that returns the list of City instances """

            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return (city_list)
