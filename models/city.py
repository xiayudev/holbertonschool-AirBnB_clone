"""
Module that
contains
City class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """Class that defines cities"""
    state_id = ""
    name = ""
