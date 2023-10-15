#!/usr/bin/python3
"""Defines City class"""


from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
