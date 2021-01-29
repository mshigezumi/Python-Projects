import sqlite3

conn = sqlite3.connect('test.db')
fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_txt STRING)") #creates the table and column in the database
    conn.commit()

for file in fileList:
    if file.endswith(".txt"): #the file name must end in .txt
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_txt) VALUES (?)", (file,)) #inserts selected files into the column
            print(file)
            conn.commit()

conn.close()
