"""
Module that
contains
User class
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class that defines users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
