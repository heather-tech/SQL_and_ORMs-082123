from __init__ import db_connection, db_cursor
from owner import Owner

class Pet:

    def __init__(self, name, species, id=None):
        self.id = id
        self.name = name
        self.species = species

    def __repr__(self):
        return f"<Pet {self.id}: {self.name} - {self.species}>"