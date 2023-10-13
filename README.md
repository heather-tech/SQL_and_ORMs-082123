# ORMs

Object-Relational Mapping is the technique of accessing a relational database using an object oriented language. Its a way for our Python programs to manage database data by "mapping" database tables to classes - and instances of classes to rows in those tables.

`class => table`

`instance => row`

By convention, we'll pluralize the name of the class to create the name of the table.

`Pet => pets`

## Methods We'll Create

For *writing to* the database:

`create_table (cls)` -> Create a table to store data related to instances of a class  
`drop_table (cls)` -> Drop (delete) the table  
`save (self)` -> Save the attributes of an object as a new table row  
`create (cls, attributes)` -> Create a new object that is an instance of `cls` and save its attributes as a new table row  
`update (self)` -> Update an object's corresponding table row  
`delete (self)` -> Delete the table row for the specified object  

----
*Question - Which of the above methods are instance methods?*  

----
<br>

For *reading from* the database:

`instance_from_db (cls, row)` -> Returns an object, aka an instance of a class, assigning the attribute values from a table row  
`get_all (cls)` -> Return a list of objects, aka instances of a class  
`find_by_id (cls, id)` -> Return an object, aka instance of a class, specified by the primary key `id`  
`find_by_name (cls, name)` -> Return an object, aka instance of a class, specified by the `name` attribute  