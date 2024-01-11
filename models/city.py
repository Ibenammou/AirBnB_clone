#!/usr/bin/python3
"""Class that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class city"""

    state_id = ""
    name = ""
