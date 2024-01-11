#!/usr/bin/python3
"""Class user that inherit from BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class inherit from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
