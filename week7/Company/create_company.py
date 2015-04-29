import sqlite3

# db = sqlite3.connect(':memory:')
db = sqlite3.connect('new_company')
cursor = db.cursor()
cursor.execute("""
CREATE TABLE company(id INTEGER PRIMARY KEY, name TEXT,
                   monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
""")
db.commit()
