import sqlite3
import re

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
                    cases TEXT,
                    cpu_cooler TEXT,
                    monitor TEXT,
                    price REAL,
                    FOREIGN KEY (user_id) REFERENCES Users(user_id)
                )
            ''')
            conn.commit()

    def add_build(self, user_id, cpu=None, mobo=None, gpu=None, ram1=None, ram2=None, 
                  hdd1=None, hdd2=None, ssd1=None, ssd2=None, psu=None, cases=None, 
                  cpu_cooler=None, monitor=None):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Dictionary mapping components to their respective price tables
            component_tables = {
                'cpu': 'CPU',
                'mobo': 'Motherboard',  # Corrected table name
                'gpu': 'GPU',
                'ram1': 'RAM',
                'ram2': 'RAM',
                'hdd1': 'HDD',
                'hdd2': 'HDD',
                'ssd1': 'SSD',
                'ssd2': 'SSD',
                'psu': 'PSU',
                'cases': 'Cases',
                'cpu_cooler': 'CPU_Coolers',
                'monitor': 'Monitors'
            }

            total_price = 0.0

            # Calculate total price by checking each component
            components = {
                'cpu': cpu,
                'mobo': mobo,
                'gpu': gpu,
                'ram1': ram1,
                'ram2': ram2,
                'hdd1': hdd1,
                'hdd2': hdd2,
                'ssd1': ssd1,
                'ssd2': ssd2,
                'psu': psu,
                'cases': cases,
                'cpu_cooler': cpu_cooler,
                'monitor': monitor
            }

            for component, value in components.items():
                if value:
                    table_name = component_tables[component]
                    cursor.execute(f'''
                        SELECT price FROM {table_name}
                        WHERE name = ?
                    ''', (value,))
                    result = cursor.fetchone()
                    if result:
                        # Use regex to remove the dollar sign and convert to float
                        price = re.sub(r'^\$', '', result[0])  # Remove the dollar sign
                        price_float = float(price)
                        total_price += price_float
                        print(f"Component: {component}, Name: {value}, Price: {price_float}")

            # Insert build with calculated price
            cursor.execute('''
                INSERT INTO Builds 
                (user_id, cpu, mobo, gpu, ram1, ram2, hdd1, hdd2, ssd1, ssd2, 
                 psu, cases, cpu_cooler, monitor, price)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (user_id, cpu, mobo, gpu, ram1, ram2, hdd1, hdd2, ssd1, ssd2,
                  psu, cases, cpu_cooler, monitor, total_price))
            
            conn.commit()

# Example usage remains the same
if __name__ == "__main__":
    build_table = BuildTable()
    build_table.create_build_table()

    build_table.add_build(
        user_id=1,
        cpu='AMD Ryzen 5 5600X',
        mobo='Asus ROG Maximus Z690',
        gpu='Radeon RX 7700 XT',
        ram1='Corsair Vengeance 16GB DDR5',
        ram2='Corsair Vengeance 16GB DDR5',
        hdd1='Seagate Barracuda 2TB',
        ssd1='Samsung 970 EVO 1TB',
        ssd2='Samsung 980 PRO 2TB',
        psu='Corsair RM850x 850W',
        cases='Be quiet! Pure Base 500DX - black',
        cpu_cooler='Arctic Freezer 34 eSports Duo , 2x 120mm - white',
        monitor='Dell UltraSharp U2723QE'
    )

    print("Build added with calculated price!")