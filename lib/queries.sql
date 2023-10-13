-- CREATE TABLE table_name (
--     id INTEGER PRIMARY KEY,
--     column_name TEXT,
--     column_name INTEGER
-- );

-- Create Table
-- Class Pet()
CREATE TABLE pets (
    id INTEGER PRIMARY KEY,
    name TEXT,
    species TEXT,
    age INTEGER,
    breed TEXT
);

-- Alter Table
-- ALTER TABLE table_name ADD COLUMN column_name TEXT;
ALTER TABLE pets ADD COLUMN color TEXT;

-- Rename Column
-- ALTER TABLE pets RENAME COLUMN color TO colorpattern;

-- Remove Table
-- DROP TABLE table_name;
-- DROP TABLE pets;

-- QUERIES
-- C => INSERT (into)
-- R => SELECT
-- U => UPDATE
-- D => DELETE

-- CREATE / INSERT (seeding)
-- INSERT INTO table_name (column_names) VALUES (new_objects_values)
INSERT INTO pets (name, species, age, breed, color) VALUES ('Jasmine', 'cat', 4, 'Siamese Mix', 'white ish');
INSERT INTO pets (name, species, age, breed, color) VALUES ('Diego', 'Mammoth', 30, 'Woolly', 'Brown');
INSERT INTO pets (name, species, age, breed, color) VALUES ('Honey', 'rabbit', 2, 'Lionhead', 'light brown');
INSERT INTO pets (name, species, age, breed, color) VALUES ('Lindley', 'dog', 7, 'Pit Bull', 'brindle and white');
INSERT INTO pets (name, species, age, breed, color) VALUES ('Clover', 'dog', 1, 'labradoole', 'apricot');
INSERT INTO pets (name, species, age, breed, color) VALUES ('Kona', 'dog', 7, 'Mutt', 'grey and black');

-- READ / SELECT
-- SELECT what_you_want FROM table_name;
-- SELECT name, breed, age FROM pets;
SELECT * FROM pets;

-- UPDATE / SET / WHERE
-- UPDATE table_name
-- SET column_name = new_value
-- WHERE condition;

UPDATE pets
SET name = 'Jazzy'
WHERE name = 'Jasmine';

-- DELETE
-- DELETE FROM table_name WHERE condition;
DELETE FROM pets
WHERE name = 'Diego';

-- One To Many
-- Author -> Books
-- Person -> Pets

-- the FOREIGN KEY lives on the table of the record which BELONGS TO a record in the other table

-- Many To Many
-- Doctor -> Appointment <- Patient
-- foreign key would live in Appointment - the join table
-- doctor_id     primary_key     patient_id

-- UberDrivers -> Rides <- Passengers
