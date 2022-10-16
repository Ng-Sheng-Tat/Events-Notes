### [EDX: CS50 SQL Lecture](https://video.cs50.io/D-1kNFO568c?screen=YR-XuGdWvR8&start=29)

- Started by introduce CSV files as a flat-file database (no hierarchy)
- Python Data Simple Sorting Functions
- Regular Expression

**Notes on RegEX in Python**
1. ``.``: any character
2. ``.*``: 0 or more characters
3. ``.+``: 1 or more characters
4. ``?``: optional
5. ``^``: start of input
6. ``$``: end of input

---

**Relational Database**
- operated by using a language called SQL (Structured Query Language)
- it does four operations, namely *CRUD*
    1. C - Create using ``CREATE, INSERT``
    2. R - Read using ``SELECT``
    3. U - Update using ``UPDATE``
    4. D - Delete using ``DELETE, DROP``

E.g.: ``CREATE TABLE tablename (column type, ...);``

**CREATE INDEX for speeding up**
- it does things fundamentally from the bottom to top using different alrorithms by manipulating the underlying datastructure
- it uses B-Tree data structure
- ``.timer on``
- ``CREATE INDEX "Title_index" ON "datacv" ("Title);``
- ``CREATE INDEX name ON table (column, ...);``

<figure>
    <center>
    <img src = "B-Tree Data Structure.png" alt = "B-Tree Data Structure">
    <figcaption>B-Tree Data Structure</figcaption>
</figure>

**Enter Into DATABASE**
- ``sqlite3 datacv.db``

**Import DATABASE**
- ``.mode csv``
- ``.import FILE TABLE``

- The design of my database is known as a *schema*
- ``.schema`` shows the schema within your database

**Notes**
1. Database name: datacv.db
2. Table name: datacv
3. Clear the sqlite3 command prompt using the code ``.shell cls``
4. Control + Z enter to escape from the sqlite3 command prompt

**SELECT Statement**
- ``SELECT COLUMNS FROM table;``
- ``SELECT Title FROM datacv;``
- ``SELECT Title, Genre FROM datacv; ``
- ``SELECT DISTINCT(UPPER(Title)) FROM datacv``

**Optional Operators in SQL**
- AVG
- COUNT
- DISTINCT
- LOWER
- MAX
- MIN
- UPPER

**SQL Filters Statement**
- WHERE
- LIKE
- ORDER BY
- LIMIT
- GROUP BY
- AS

**SELECT Statement With Filters**
-  ``SELECT Title From datacv limit 10;``
- ``SELECT Title FROM datacv WHERE Title LIKE "Thor";``
- ``SELECT Title FROM datacv WHERE Title = "Thor";``
- ``SELECT Title FROM datacv WHERE Title LIKE "%Thor%";``
- ``SELECT COUNT(*) AS counter FROM datacv WHERE Title LIKE "%Thor%";``

**DELETE statement**
- ``DELETE FROM datacv WHERE Title LIKE "Thor";``

**UPDATE statement**
- ``SELECT Title FROM datacv WHERE Title = "Gundam 00"``
- ``UPDATE datacv SET Title = "Gundam - 00" WHERE Title = "Gundam 00"``
- ``SELECT Title FROM datacv WHERE Title = "Gundam 00"``

**Concatenation of filters**
- ``OR``
- ``NOT``
- ``AND``
- ``WHERE SOMETHING IN (ANOTHER QUERIES)``

**PRIMARY KEY**
- uniques row (identifier) id that uses to relate two different tables in the same database

**Foreign Key**
- uniques identified in other tables that relates to the primary key
- this is what we know as the relational database

**INSERT Statement**
- ``INSERT INTO datacv (Title) VALUES ("Final Fantasty");``
- ``INSERT INTO datacv (Title, Genre) VALUES ("Final Fantasty", "Fighting");``

**SQLITE 3 Syntax**
- ``db.execute(" ? ", Title)``

**Datatype in SQL**
- BLOB (Binary objects like files)
- INTEGER
- NUMERIC
- REAL
- TEXT

**JOIN**
- ``SELECT Title FROM table1 JOIN Title2 FROM table2 ON table1.id = table2.id``
- ``SELECT Title FROM table1, table2 WHERE table1.id = table2.id``

- In Computer Science, increating time complexity often reduces in space complexity and vice versa, the design should be finding the inflexion point (balance point) of it

- ``--`` this is a comment in SQL

- **SQL Injection Attact**, where the users deliberately type in SQL command and let the database being hacked
- **Race Condition** where the checking of the state by two different cases and gets update similarly which should not be the same like the refrigerator case, solved by introducing *locks* and *transactions*