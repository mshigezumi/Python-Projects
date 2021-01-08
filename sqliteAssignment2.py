import sqlite3
"""
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
              (45, 'Luigi', 'Vercoti'))
"""

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43),('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)

