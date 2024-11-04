import sqlite3

# Step 1: Connect to SQLite database
# This will create a new database file named 'testdb.sqlite' if it doesn't already exist
conn = sqlite3.connect('testdb.sqlite')

# Step 2: Create a cursor object
cur = conn.cursor()

# Step 3: Create a table
cur.execute('''
    CREATE TABLE IF NOT EXISTS emp (
        empid INTEGER PRIMARY KEY,
        empname TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Step 4: Insert sample data
sample_data = [
    (1, 'Alice Smith', 'alice.smith@example.com'),
    (2, 'Bob Johnson', 'bob.johnson@example.com'),
    (3, 'Charlie Brown', 'charlie.brown@example.com'),
    (4, 'Diana Prince', 'diana.prince@example.com')
]

cur.executemany('INSERT OR IGNORE INTO emp (empid, empname, email) VALUES (?, ?, ?)', sample_data)

# Step 5: Query the table and print results
cur.execute('SELECT * FROM emp')
rows = cur.fetchall()

print("Employee Table Data:")
for row in rows:
    print(row)

# Step 6: Commit changes and close the connection
conn.commit()
conn.close()
