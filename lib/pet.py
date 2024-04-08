from __init__ import db_connection, db_cursor


class Pet:

    all = {}

    def __init__(self, name, species, owner_id, id=None):
        self.id = id
        self.name = name
        self.species = species
        self.owner_id = owner_id

    def __repr__(self):
        return f"<Pet {self.id}: {self.name} - {self.species}>"
    
    @classmethod #decorator
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owners(id))
        """
        db_cursor.execute(sql)
        db_connection.commit()

    @classmethod #decorator
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS pets
        """
        db_cursor.execute(sql)
        db_connection.commit()

    def save(self):
        sql = """
            INSERT INTO pets (name, species, owner_id)
            VALUES (?, ?, ?)
        """

        db_cursor.execute(sql, (self.name, self.species, self.owner_id))
        db_connection.commit()

        self.id = db_cursor.lastrowid

        Pet.all[self.id] = self

    @classmethod
    def create(cls, name, species, owner_id):
        # equiavalent to Pet(name, species, owner_id)
        pet = cls(name, species, owner_id)
        pet.save()
        return pet
        
    def update(self):
        sql = """
            UPDATE pets
            set name = ?, species = ?, owner_id = ?
            WHERE id = ?
        """

        db_cursor.execute(sql, (self.name, self.species, self.owner_id, self.id))
        db_connection.commit()

    def delete(self):
        sql = """
            DELETE FROM pets
            WHERE id = ?
        """

        db_cursor.execute(sql, (self.id, ))
        db_connection.commit()

        del Pet.all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        # first - check the dictionary for an existing isntance of a pet, using the primary key
        pet = cls.all.get(row[0])

        if pet:
            pet.name = row[1]
            pet.species = row[2]
            pet.owner_id = row[3]
        else: 
            #nothing was found, we should create a new isntance and add it to our dictionary
            pet = cls(row[1], row[2], row[3])
            pet.id = row[0]
            cls.all[pet.id] = pet
        return pet
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM pets
        """

        rows = db_cursor.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM pets
            WHERE id = ?
        """

        row = db_cursor.execute(sql, (id, )).fetchone()

        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM pets
            WHERE name = ?
        """

        row = db_cursor.execute(sql, (name, )).fetchone()

        return cls.instance_from_db(row) if row else None
    
    def owner(self):
        from owner import Owner

        sql = """
            SELECT * FROM owners
            WHERE id = ?
        """

        row = db_cursor.execute(sql, (self.owner_id, )).fetchone()

        owner = Owner.instance_from_db(row)
        return owner