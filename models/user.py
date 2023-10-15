#!/usr/bin/python3
"""Defines the User class."""


from models.base_model import BaseModel


class User(BaseModel):
    """Creates a user.

    Attributes:
        email (str): The email of each user.
        password (str): The password of each user.
        first_name (str): The first name of the user.
        last_name (str): The last name of user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
