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
                    Threads INTEGER,
                    Price TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Motherboard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Socket TEXT,
                    Chipset TEXT,
                    Price TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS GPU (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Series TEXT,
                    VRAM TEXT,
                    TDP TEXT,
                    Price TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS RAM (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Type TEXT,
                    Bus_Speed TEXT,
                    Quantity TEXT,
                    Price TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS HDD (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    RPM TEXT,
                    Price TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS SSD (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Bus TEXT,
                    Format TEXT,
                    Price TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS PSU (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Wattage TEXT,
                    Price TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Cases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Price TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS CPU_Coolers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Socket TEXT,
                    Price TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Monitors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT,
                    Size TEXT,
                    Resolution TEXT,
                    Price TEXT
                )
            ''')

    def load_json_data(self, filename):
        file_path = os.path.join(self.json_folder_path, filename)
        with open(file_path, "r") as file:
            return json.load(file)

    def insert_data(self, table, data):
        # Each thread opens its own connection for thread safety
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            if table == "CPU":
                cursor.execute('''
                    INSERT INTO CPU (Name, Socket, Clock_Speed, Turbo_Speed, Cores, Threads, Price)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (data["Name"], data["Socket"], data["Clock Speed"], data["Turbo Speed"], data["Cores"], data["Threads"], data["Price"]))

            elif table == "Motherboard":
                cursor.execute('''
                    INSERT INTO Motherboard (Name, Size, Socket, Chipset, Price)
                    VALUES (?, ?, ?, ?, ?)
                ''', (data["Name"], data["Size"], data["Socket"], data["Chipset"], data["Price"]))

            elif table == "GPU":
                cursor.execute('''
                    INSERT INTO GPU (Name, Series, VRAM, TDP, Price)
                    VALUES (?, ?, ?, ?, ?)
                ''', (data["Name"], data["Series"], data["VRAM"], data["TDP"], data["Price"]))

            elif table == "RAM":
                cursor.execute('''
                    INSERT INTO RAM (Name, Size, Type, Bus_Speed, Quantity, Price)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (data["Name"], data["Size"], data["Type"], data["Bus Speed"], data["Quantity"], data["Price"]))

            elif table == "HDD":
                cursor.execute('''
                    INSERT INTO HDD (Name, Size, RPM, Price)
                    VALUES (?, ?, ?, ?)
                ''', (data["Name"], data["Size"], data["RPM"], data["Price"]))

            elif table == "SSD":
                cursor.execute('''
                    INSERT INTO SSD (Name, Size, Bus, Format, Price)
                    VALUES (?, ?, ?, ?, ?)
                ''', (data["Name"], data["Size"], data["Bus"], data["Format"], data["Price"]))

            elif table == "PSU":
                cursor.execute('''
                    INSERT INTO PSU (Name, Size, Wattage, Price)
                    VALUES (?, ?, ?, ?)
                ''', (data["Name"], data["Size"], data["Wattage"], data["Price"]))

            elif table == "Cases":
                cursor.execute('''
                    INSERT INTO Cases (Name, Size, Price)
                    VALUES (?, ?, ?)
                ''', (data["Name"], data["Size"], data["Price"]))

            elif table == "CPU_Coolers":
                cursor.execute('''
                    INSERT INTO CPU_Coolers (Name, Socket, Price)
                    VALUES (?, ?, ?)
                ''', (data["Name"], data["Socket"], data["Price"]))

            elif table == "Monitors":
                cursor.execute('''
                    INSERT INTO Monitors (Name, Size, Resolution, Price)
                    VALUES (?, ?, ?, ?)
                ''', (data["Name"], data["Size"], data["Resolution"], data["Price"]))

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting data into {table}: {e}")
        finally:
            if conn:
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
            "psu_data.json": "PSU",
            "cases_data.json": "Cases",
            "cpu_coolers_data.json": "CPU_Coolers",
            "monitors_data.json": "Monitors"
        }

        threads = []
        for filename, table_name in files_to_tables.items():
            # Each thread processes one file and inserts its data
            thread = threading.Thread(target=self.store_data_from_file, args=(filename, table_name))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
