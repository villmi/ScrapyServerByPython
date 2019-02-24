import sqlite3

con = sqlite3.connect('test.db')

print('open sqlite successfully!')

c = con.cursor()

sql = 'select * from company where id="100"'
c.execute(sql)
print(c.fetchone())




