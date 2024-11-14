import sqlite3
from CPU_And_Motherboard_Data_Classes import *  

class CompatibilityManager:
    def __init__(self, db_path='data/database/database.sqlite'):
        self.db_path = db_path

    def get_compatible_motherboards(self, cpu_id):
        """Retrieve compatible motherboards based on the CPU's socket type."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Step 1: Get socket type for the selected CPU
            cursor.execute("SELECT Socket FROM CPU WHERE id = ?", (cpu_id,))
            result = cursor.fetchone()
            
            cpu_socket_type = result[0]
            
            # Step 2: Fetch all motherboards with matching socket type
            cursor.execute("SELECT * FROM Motherboard WHERE Socket = ?", (cpu_socket_type,))
            compatible_motherboards = [Motherboard(*row) for row in cursor.fetchall()]
            
            return compatible_motherboards

    def get_compatible_cpus(self, motherboard_id):
        """Retrieve compatible CPUs based on the motherboard's socket type."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            
            cursor.execute("SELECT Socket FROM Motherboard WHERE id = ?", (motherboard_id,))
            result = cursor.fetchone() 
            
            motherboard_socket_type = result[0]
            
            cursor.execute("SELECT * FROM CPU WHERE Socket = ?", (motherboard_socket_type,))
            compatible_cpus = [CPU(*row) for row in cursor.fetchall()]
            
            return compatible_cpus
