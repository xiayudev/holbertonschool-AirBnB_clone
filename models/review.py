"""
Module that
contains
Review class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class that defines reviews"""
    place_id = ""
    user_id = ""
    text = ""
