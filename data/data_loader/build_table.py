import sqlite3

class BuildTable:
    def __init__(self, db_path="data/database/database.sqlite"):
        self.db_path = db_path
    
    def create_build_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Builds (
                    user_id INTEGER NOT NULL,
                    build_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpu TEXT,
                    mobo TEXT,
                    gpu TEXT,
                    ram1 TEXT,
                    ram2 TEXT,
                    hdd1 TEXT,
                    hdd2 TEXT,
                    ssd1 TEXT,
                    ssd2 TEXT,
                    FOREIGN KEY (user_id) REFERENCES Users(user_id)
                )
            ''')
            conn.commit()

    def add_build(self, user_id, cpu=None, mobo=None, gpu=None, ram1=None, ram2=None, 
                  hdd1=None, hdd2=None, ssd1=None, ssd2=None):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO Builds (user_id, cpu, mobo, gpu, ram1, ram2, hdd1, hdd2, ssd1, ssd2)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, cpu, mobo, gpu, ram1, ram2, hdd1, hdd2, ssd1, ssd2))
            
            conn.commit()

# Example usage:
build_table = BuildTable()
build_table.create_build_table()

# Add a build (some parts can be NULL)
build_table.add_build(user_id=1, cpu='Intel i9', mobo='Asus Z490', gpu='NVIDIA RTX 3080', ram1='siuuuu', ram2='siuuuu2')
