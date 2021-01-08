import sqlite3

def db():
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("CREATE TABLE Roster (Name, Species, IQ)")
    values = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))
    cur.executemany("INSERT INTO Roster VALUES (?, ?, ?)", values)
    cur.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print(row)

db()
