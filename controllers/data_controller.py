import sqlite3
import json
import os
import threading

class DataController:
    def __init__(self, db_path="data/database/database.sqlite"):
        self.db_path = db_path
        self.json_folder_path = "data/json"
        self.create_tables()

    def create_tables(self):
        # Create tables if they do not exist
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS CPU (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Socket TEXT,
                    Clock_Speed TEXT,
                    Turbo_Speed TEXT,
                    Cores INTEGER,
                    Threads INTEGER
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Motherboard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Socket TEXT,
                    Chipset TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS GPU (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Series TEXT,
                    VRAM TEXT,
                    TDP TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS RAM (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Type TEXT,
                    Bus_Speed TEXT,
                    Quantity TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS HDD (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    RPM TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS SSD (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Bus TEXT,
                    Format TEXT
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS PSU (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Wattage TEXT
                )
            ''')

    def load_json_data(self, filename):
        file_path = os.path.join(self.json_folder_path, filename)
        with open(file_path, "r") as file:
            return json.load(file)

    def insert_data(self, table, data):
        try:
            conn = sqlite3.connect(self.db_path, check_same_thread=False)
            cursor = conn.cursor()

            if table == "CPU":
                cursor.execute('''
                    INSERT INTO CPU (Name, Socket, Clock_Speed, Turbo_Speed, Cores, Threads)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (data["Name"], data["Socket"], data["Clock Speed"], data["Turbo Speed"], data["Cores"], data["Threads"]))
            
            elif table == "Motherboard":
                cursor.execute('''
                    INSERT INTO Motherboard (Name, Size, Socket, Chipset)
                    VALUES (?, ?, ?, ?)
                ''', (data["Name"], data["Size"], data["Socket"], data["Chipset"]))

            elif table == "GPU":
                cursor.execute('''
                    INSERT INTO GPU (Name, Series, VRAM, TDP)
                    VALUES (?, ?, ?, ?)
                ''', (data["Name"], data["Series"], data["VRAM"], data["TDP"]))

            elif table == "RAM":
                cursor.execute('''
                    INSERT INTO RAM (Name, Size, Type, Bus_Speed, Quantity)
                    VALUES (?, ?, ?, ?, ?)
                ''', (data["Name"], data["Size"], data["Type"], data["Bus Speed"], data["Quantity"]))

            elif table == "HDD":
                cursor.execute('''
                    INSERT INTO HDD (Name, Size, RPM)
                    VALUES (?, ?, ?)
                ''', (data["Name"], data["Size"], data["RPM"]))

            elif table == "SSD":
                cursor.execute('''
                    INSERT INTO SSD (Name, Size, Bus, Format)
                    VALUES (?, ?, ?, ?)
                ''', (data["Name"], data["Size"], data["Bus"], data["Format"]))

            elif table == "PSU":
                cursor.execute('''
                    INSERT INTO PSU (Name, Size, Wattage)
                    VALUES (?, ?, ?)
                ''', (data["Name"], data["Size"], data["Wattage"]))

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting data into {table}: {e}")
        finally:
            conn.close()

    def store_data_from_file(self, filename, table_name):
        data_list = self.load_json_data(filename)
        for data in data_list:
            self.insert_data(table_name, data)

    def store_all_data(self):
        files_to_tables = {
            "cpu_data.json": "CPU",
            "mobo_data.json": "Motherboard",
            "gpu_data.json": "GPU",
            "ram_data.json": "RAM",
            "hdd_data.json": "HDD",
            "ssd_data.json": "SSD",
            "psu_data.json": "PSU"
        }

        threads = []
        for filename, table_name in files_to_tables.items():
            thread = threading.Thread(target=self.store_data_from_file, args=(filename, table_name))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

