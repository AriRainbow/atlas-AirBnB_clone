#!/usr/bin/python3
""" Review Module for the AirBnB clone project """

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel"""
    text = ""
    place_id = ""
    user_id = ""
