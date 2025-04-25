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
                    psu TEXT,
                    "case" TEXT,  -- Escaped the reserved keyword
                    cpu_cooler TEXT,
                    monitor TEXT,
                    FOREIGN KEY (user_id) REFERENCES Users(user_id)
                )
            ''')
            conn.commit()

    def add_build(self, user_id, cpu=None, mobo=None, gpu=None, ram1=None, ram2=None, 
                  hdd1=None, hdd2=None, ssd1=None, ssd2=None, psu=None, case=None, 
                  cpu_cooler=None, monitor=None):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO Builds (user_id, cpu, mobo, gpu, ram1, ram2, hdd1, hdd2, ssd1, ssd2, psu, "case", cpu_cooler, monitor)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, cpu, mobo, gpu, ram1, ram2, hdd1, hdd2, ssd1, ssd2, psu, case, cpu_cooler, monitor))
            
            conn.commit()

# Example usage:
if __name__ == "__main__":
    build_table = BuildTable()
    build_table.create_build_table()

    # Add a build (some parts can be NULL)
    build_table.add_build(
        user_id=1,
        cpu='Intel Core i9-12900K',
        mobo='Asus ROG Maximus Z690',
        gpu='NVIDIA GeForce RTX 4090',
        ram1='Corsair Vengeance 16GB DDR5',
        ram2='Corsair Vengeance 16GB DDR5',
        hdd1='Seagate Barracuda 2TB',
        hdd2=None,
        ssd1='Samsung 970 EVO 1TB',
        ssd2='Samsung 980 PRO 2TB',
        psu='Corsair RM850x 850W',
        case='NZXT H510 Elite',
        cpu_cooler='Noctua NH-D15',
        monitor='Dell UltraSharp U2723QE'
    )
    print("Build added successfully!")