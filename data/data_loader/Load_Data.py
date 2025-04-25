import re
from bs4 import BeautifulSoup
import requests
import threading
import json
import random

class PCComponentScraper:
    def __init__(self):
        self.urls = {
            "cpu": "https://www.pc-kombo.com/ca/components/cpus",
            "mobo": "https://www.pc-kombo.com/ca/components/motherboards",
            "gpu": "https://www.pc-kombo.com/ca/components/gpus",
            "ram": "https://www.pc-kombo.com/ca/components/rams",
            "hdd": "https://www.pc-kombo.com/ca/components/hdds",
            "ssd": "https://www.pc-kombo.com/ca/components/ssds",
            "psu": "https://www.pc-kombo.com/ca/components/psus",
            "cases": "https://www.pc-kombo.com/ca/components/cases",
            "cpu_coolers": "https://www.pc-kombo.com/ca/components/cpucoolers",
            "monitors": "https://www.pc-kombo.com/ca/components/displays"
        }
    def save_to_json(self, filename, data):
        filepath = f"data/json/{filename}"
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

    def generate_price(self, min_price, max_price, increment):
        return random.randrange(min_price, max_price + increment, increment)

    
    def extract_cpu(self):
        cpu_data = []

        response = requests.get(self.urls["cpu"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            cpu_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            for cpu in cpu_list:
                name = cpu.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = cpu.find("div", class_="subtitle")
                
                socket = "N/A"
                clock_speed = "N/A"
                turbo_speed = "N/A"
                cores = "N/A"
                threads = "N/A"
                

                subtitle_text = subtitle.get_text(separator=' ', strip=True)

                # Use regex to extract values
                socket_match = re.search(r'Socket\s*([^\s]+)', subtitle_text)
                if socket_match:
                    socket = socket_match.group(1)

                clock_speed_match = re.search(r'Clock\s*([\d.]+ GHz)', subtitle_text)
                if clock_speed_match:
                    clock_speed = clock_speed_match.group(1)

                turbo_speed_match = re.search(r'Turbo\s*([\d.]+ GHz)', subtitle_text)
                if turbo_speed_match:
                    turbo_speed = turbo_speed_match.group(1)

                cores_match = re.search(r'(\d+)\s*Cores', subtitle_text)
                if cores_match:
                    cores = cores_match.group(1)

                threads_match = re.search(r'(\d+)\s*Threads', subtitle_text)
                if threads_match:
                    threads = threads_match.group(1)
                
                price = self.generate_price(100, 1200, 50)
                cpu_data.append({
                    "Name": name,
                    "Socket": socket,
                    "Clock Speed": clock_speed,
                    "Turbo Speed": turbo_speed,
                    "Cores": cores,
                    "Threads": threads,
                    "Price": f"${price}"
                })
                self.save_to_json("cpu_data.json", cpu_data)

        else:
            print("Failed to retrieve data.")

    def extract_mobo(self):
        mobo_data = []
        response = requests.get(self.urls["mobo"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            mobo_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            
            for mobo in mobo_list:
                name = mobo.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = mobo.find("div", class_="subtitle")

                size = "N/A"
                socket = "N/A"
                chipset = "N/A"
                
                size_span = subtitle.find("span", class_="size")
                if size_span:
                    size = size_span.text.strip() 
                
                subtitle_text = subtitle.get_text(separator=' ', strip=True)

                size_match = re.search(r'Size\s*([^\s]+)', subtitle_text)
                if size_match:
                    size = size_match.group(1)

                socket_match = re.search(r'Socket\s*([^\s]+)', subtitle_text)
                if socket_match:
                    socket = socket_match.group(1)

                chipset_match = re.search(r'Chipset\s*([^\s]+)', subtitle_text)
                if chipset_match:
                    chipset = chipset_match.group(1)
                
                price = self.generate_price(75, 1200, 25)

                mobo_data.append({
                    "Name": name,
                    "Size": size,
                    "Socket": socket,
                    "Chipset": chipset,
                    "Price": f"${price}"
                })
                self.save_to_json("mobo_data.json", mobo_data)
        else:
            print("Failed to retrieve data.")

    def extract_gpu(self):
        gpu_data = []
        response = requests.get(self.urls["gpu"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            gpu_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            
            for gpu in gpu_list:
                # Extracting the GPU name
                name = gpu.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = gpu.find("div", class_="subtitle")
                
                # Initialize default values
                series = "N/A"
                vram = "N/A"
                tdp = "N/A"
                
                # Extract series and VRAM from spans
                series_span = subtitle.find("span", class_="series")
                if series_span:
                    series = series_span.text.strip()
                
                vram_span = subtitle.find("span", class_="vram")
                if vram_span:
                    vram = vram_span.text.strip()
                    
                # Extract TDP as the last numeric value in subtitle text
                subtitle_text = subtitle.get_text(separator=' ', strip=True)
                tdp_match = re.search(r'(\d+)\s*W$', subtitle_text)
                if tdp_match:
                    tdp = tdp_match.group(1)

                price = self.generate_price(200, 2000, 50)
                gpu_data.append({
                    "Name": name,
                    "Series": series,
                    "VRAM": vram,
                    "TDP": f"{tdp}W",
                    "Price": f"${price}"
                })
                self.save_to_json("gpu_data.json", gpu_data)

        else:
            print("Failed to retrieve data.")

    def extract_ram(self):
        ram_data = []
        response = requests.get(self.urls["ram"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            ram_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            
            for ram in ram_list:
                # Extracting the RAM name
                name = ram.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = ram.find("div", class_="subtitle")
                
                # Initialize default values
                size = "N/A"
                ram_type = "N/A"
                bus_speed = "N/A"
                quantity = "N/A"
                
                # Extract size from span
                size_span = subtitle.find("span", class_="size")
                if size_span:
                    size = size_span.text.strip()
                
                # Extract type and bus speed using regex
                type_span = subtitle.find("span", class_="type")
                if type_span:
                    type_text = type_span.text.strip()
                    # Use regex to separate type (DDR) and speed
                    type_match = re.search(r'(DDR\d)-(\d+)', type_text)
                    if type_match:
                        ram_type = type_match.group(1)
                        bus_speed = type_match.group(2) + " MHz"  # Add MHz to the speed

                # Extract quantity as the last part of the subtitle text
                subtitle_text = subtitle.get_text(separator=' ', strip=True)
                quantity_parts = subtitle_text.split()
                if quantity_parts:
                    quantity = quantity_parts[-1]  # Get the last part for quantity

                price = self.generate_price(50, 500, 5)

                ram_data.append({
                    "Name": name,
                    "Size": size,
                    "Type": ram_type,
                    "Bus Speed": bus_speed,
                    "Quantity": quantity,
                    "Price": f"${price}"
                })
                self.save_to_json("ram_data.json", ram_data)
        else:
            print("Failed to retrieve data.")


    def extract_hdd(self):
        hdd_data = []
        response = requests.get(self.urls["hdd"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            hdd_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            
            for hdd in hdd_list:
                # Extracting the HDD name
                name = hdd.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = hdd.find("div", class_="subtitle")
                
                # Initialize default values
                size = "N/A"
                rpm = "N/A"
                
                # Extract size and RPM from spans
                size_span = subtitle.find("span", class_="size")
                if size_span:
                    size = size_span.text.strip()
                
                rpm_span = subtitle.find("span", class_="rpm")
                if rpm_span:
                    rpm = rpm_span.text.strip()
                    
                price = self.generate_price(40, 300, 10)
                hdd_data.append({
                    "Name": name,
                    "Size": size,
                    "RPM": rpm,
                    "Price": f"${price}"
                })
                self.save_to_json("hdd_data.json", hdd_data)
        else:
            print("Failed to retrieve data.")

    def extract_ssd(self):
        ssd_data = []
        response = requests.get(self.urls["ssd"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            ssd_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            
            for ssd in ssd_list:
                # Extracting the SSD name
                name = ssd.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = ssd.find("div", class_="subtitle")
                
                # Initialize default values
                size = "N/A"
                bus = "N/A"
                format_type = "N/A"
                
                # Extract size, bus, and format from spans
                size_span = subtitle.find("span", class_="size")
                if size_span:
                    size = size_span.text.strip()
                
                bus_span = subtitle.find("span", class_="bus")
                if bus_span:
                    bus = bus_span.text.strip()
                if bus == "NVM":
                    bus = "NVME"
                    
                # Extract format (e.g., "M.2 Format")
                format_match = re.search(r'(\S+ Format)', subtitle.get_text(separator=' ', strip=True))
                if format_match:
                    format_type = format_match.group(1)

                price = self.generate_price(50, 600, 10)

                ssd_data.append({
                    "Name": name,
                    "Size": size,
                    "Bus": bus,
                    "Format": format_type,
                    "Price": f"${price}"
                })
                self.save_to_json("ssd_data.json", ssd_data)
        else:
            print("Failed to retrieve data.")

    def extract_psu(self):
        psu_data = []
        response = requests.get(self.urls["psu"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            psu_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            
            for psu in psu_list:
                # Extracting the PSU name
                name = psu.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = psu.find("div", class_="subtitle")
                
                # Initialize default values
                size = "N/A"
                wattage = "N/A"
                
                # Extract size and wattage from spans
                size_span = subtitle.find("span", class_="size")
                if size_span:
                    size = size_span.text.strip()
                
                watt_span = subtitle.find("span", class_="watt")
                if watt_span:
                    wattage = watt_span.text.strip()

                price = self.generate_price(100, 1200, 50)
                # Print the extracted details
                psu_data.append({
                    "Name": name,
                    "Size": size,
                    "Wattage": wattage,
                    "Price": f"${price}"
                })
                self.save_to_json("psu_data.json", psu_data)
        else:
            print("Failed to retrieve data.")

    def extract_cases(self):
        cases_data = []
        response = requests.get(self.urls["cases"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            cases_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            
            for case in cases_list:
                name = case.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = case.find("div", class_="subtitle")
                size = "N/A"
                subtitle_text = subtitle.get_text(separator=' ', strip=True)
                
                size_match = re.search(r'Size\s*([^\s]+)', subtitle_text)
                if size_match:
                    size = size_match.group(1)

                price = self.generate_price(30, 500, 10)
                cases_data.append({
                    "Name": name,
                    "Size": size,
                    "Price": f"${price}"
                })
                self.save_to_json("cases_data.json", cases_data)
        else:
            print("Failed to retrieve data for cases.")

    
    def extract_cpu_coolers(self):
        coolers_data = []
        response = requests.get(self.urls["cpu_coolers"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            coolers_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            
            for cooler in coolers_list:
                name = cooler.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = cooler.find("div", class_="subtitle")
                socket = "N/A"
                subtitle_text = subtitle.get_text(separator=' ', strip=True)
                
                socket_match = re.search(r'Socket\s*([^\s]+)', subtitle_text)
                if socket_match:
                    socket = socket_match.group(1)

                price = self.generate_price(20, 150, 10)

                coolers_data.append({
                    "Name": name,
                    "Socket": socket,
                    "Price": f"${price}"
                })
                self.save_to_json("cpu_coolers_data.json", coolers_data)
        else:
            print("Failed to retrieve data for CPU coolers.")

    def extract_monitors(self):
        monitors_data = []
        response = requests.get(self.urls["monitors"])

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            monitors_list = soup.find_all("div", class_="column col-10 col-lg-8 col-sm-12")
            
            for monitor in monitors_list:
                name = monitor.find("h5", class_="name")
                name = name.text.strip() if name else "Not Found"
                
                subtitle = monitor.find("div", class_="subtitle")
                size = "N/A"
                resolution = "N/A"
                subtitle_text = subtitle.get_text(separator=' ', strip=True)
                
                size_match = re.search(r'(\d+\.?\d*)\s*inch', subtitle_text)
                if size_match:
                    size = size_match.group(1) + " inch"

                resolution_match = re.search(r'(\d+x\d+)', subtitle_text)
                if resolution_match:
                    resolution = resolution_match.group(1)

                price = self.generate_price(100, 1200, 50)

                monitors_data.append({
                    "Name": name,
                    "Size": size,
                    "Resolution": resolution,
                    "Price": f"${price}"
                })
                self.save_to_json("monitors_data.json", monitors_data)
        else:
            print("Failed to retrieve data for monitors.")

    def scrape_all(self):
        functions = [
            self.extract_cpu,
            self.extract_mobo,
            self.extract_gpu,
            self.extract_ram,
            self.extract_hdd,
            self.extract_ssd,
            self.extract_psu,
            self.extract_cases,
            self.extract_cpu_coolers,
            self.extract_monitors
        ]

        threads = []

        for func in functions:
            thread = threading.Thread(target=func)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        

# Example usage
if __name__ == "__main__":
    scraper = PCComponentScraper()
    scraper.scrape_all()
