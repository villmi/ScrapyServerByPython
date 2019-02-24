import sqlite3

con = sqlite3.connect('test.db')

print('open sqlite successfully!')

c = con.cursor()

sql = '''CREATE TABLE "query" (id INT PRIMARY KEY NOT NULL,' 
      word TEXT, 
      tablename TEXT, 
      state INT NOT NULL, 
      completed INT NOT NULL,'
      total INT NOT NULL
      );'''
c.execute(sql)
print(c.fetchone())




