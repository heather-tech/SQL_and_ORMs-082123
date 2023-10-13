from __init__ import db_connection, db_cursor

class Owner:

    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Owner {self.id}: {self.name}>"
    
    #### Writing to the db ####
    
    @classmethod
    def create_table(cls):
        """ Create a new table to store owner instances """

        sql = """
            CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        db_cursor.execute(sql)
        db_connection.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop (delete) the table that stores owner instances """
        
        sql = """
            DROP TABLE IF EXISTS owners;
        """
        db_cursor.execute(sql)
        db_connection.commit()

    def save(self):
        sql = """
            INSERT INTO owners (name)
            VALUES (?)
        """

        db_cursor.execute(sql, (self.name, ))
        db_connection.commit()

        self.id = db_cursor.lastrowid
        Owner.all[self.id] = self

    @classmethod
    def create(cls, name):
        # equivalent to Owner(name)
        owner = cls(name)
        owner.save()
        return owner
    
    def update(self):
        sql = """
            UPDATE owners
            SET name = ?
            WHERE id = ?
        """

        db_cursor.execute(sql, (self.name, self.id))
        db_connection.commit()

    def delete(self):
        sql = """
            DELETE FROM owners
            WHERE id = ?
        """

        db_cursor.execute(sql, (self.id, ))
        db_connection.commit()

    #### Retrieving from the db ####

    @classmethod
    def instance_from_db(cls, row):
        # first check the dictionary for an existing instance, using the row's primary key
        owner = cls.all.get(row[0])

        if owner:
            # make sure attributes match, in case the python object was modified
            owner.name = row[1]
        else:
            # nothing found in the dictionary, we can create a new instance and add it to the dictionary
            owner = cls(row[1])
            owner.id = row[0]
            cls.all[owner.id] = owner
        return owner
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM owners
        """

        rows = db_cursor.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM owners
            WHERE id = ?
        """

        row = db_cursor.execute(sql, (id, )).fetchone()

        return cls.instance_from_db(row) if row else None
    
    #### Retrieving Pets associated with this owner ####

    def pets(self):
        from pet import Pet

        sql = """
            SELECT * FROM pets
            WHERE owner_id = ?
        """

        db_cursor.execute(sql, (self.id, ))

        rows = db_cursor.fetchall()
        return [Pet.instance_from_db(row) for row in rows]
