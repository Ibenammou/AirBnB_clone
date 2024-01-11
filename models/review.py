#!/usr/bin/python3
"""Class that inherit from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class review"""

    place_id = ""
    user_id = ""
    text = ""
