import re
from bs4 import BeautifulSoup
import requests
import time
import threading

url1 = "https://www.pc-kombo.com/ca/components/cpus"
url2 = "https://www.pc-kombo.com/ca/components/motherboards"
url3 = "https://www.pc-kombo.com/ca/components/gpus"
url4 = "https://www.pc-kombo.com/ca/components/rams"
url5 = "https://www.pc-kombo.com/ca/components/hdds"
url6 = "https://www.pc-kombo.com/ca/components/ssds"
url7 = "https://www.pc-kombo.com/ca/components/psus"

seq_time = 0
mult_time = 0

def extract_cpu(url):

    response = requests.get(url)

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

            print(f"Name: {name}")
            print(f"Socket: {socket}")
            print(f"Clock Speed: {clock_speed}")
            print(f"Turbo Speed: {turbo_speed if turbo_speed != 'Not Found' else 'N/A'}")
            print(f"Cores: {cores}")
            print(f"Threads: {threads}")
            print("-" * 40)
    else:
        print("Failed to retrieve data.")


def extract_mobo(url):
    response = requests.get(url)

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

            print(f"Name: {name}")
            print(f"Size: {size}")
            print(f"Socket: {socket}")
            print(f"Chipset: {chipset}")
            print("-" * 40)
    else:
        print("Failed to retrieve data.")

def extract_gpu(url):
    response = requests.get(url)

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

            # Print the extracted details
            print(f"Name: {name}")
            print(f"Series: {series}")
            print(f"VRAM: {vram}")
            print(f"TDP: {tdp}W")
            print("-" * 40)
    else:
        print("Failed to retrieve data.")

def extract_ram(url):
    response = requests.get(url)

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

            # Print the extracted details
            print(f"Name: {name}")
            print(f"Size: {size}")
            print(f"Type: {ram_type}")
            print(f"Bus Speed: {bus_speed}")
            print(f"Quantity: {quantity}")
            print("-" * 40)
    else:
        print("Failed to retrieve data.")


def extract_hdd(url):
    response = requests.get(url)

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
                
            # Print the extracted details
            print(f"Name: {name}")
            print(f"Size: {size}")
            print(f"RPM: {rpm}")
            print("-" * 40)
    else:
        print("Failed to retrieve data.")

def extract_ssd(url):
    response = requests.get(url)

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
                
            # Extract format (e.g., "M.2 Format")
            format_match = re.search(r'(\S+ Format)', subtitle.get_text(separator=' ', strip=True))
            if format_match:
                format_type = format_match.group(1)

            # Print the extracted details
            print(f"Name: {name}")
            print(f"Size: {size}")
            print(f"Bus: {bus}")
            print(f"Format: {format_type}")
            print("-" * 40)
    else:
        print("Failed to retrieve data.")

def extract_psu(url):
    response = requests.get(url)

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

            # Print the extracted details
            print(f"Name: {name}")
            print(f"Size: {size}")
            print(f"Wattage: {wattage}")
            print("-" * 40)
    else:
        print("Failed to retrieve data.")

def main_sequential():
    global seq_time

    start_time = time.time()
    # extract_cpu(url1)
    extract_mobo(url2)
    # extract_gpu(url3)
    # extract_ram(url4)
    # extract_hdd(url5)
    extract_ssd(url6)
    extract_psu(url7)

    end_time = time.time()
    elapsed_time = end_time - start_time
    seq_time = elapsed_time
    
    # print(f"Total time taken to execute all functions: {elapsed_time:.2f} seconds")

def main_multithreaded():
    global mult_time

    start_time = time.time()
    functions = [
        lambda: extract_cpu(url1),
        lambda: extract_mobo(url2),
        lambda: extract_gpu(url3),
        lambda: extract_ram(url4),
        lambda: extract_hdd(url5),
        lambda: extract_ssd(url6),
        lambda: extract_psu(url7)
    ]
    
    threads = []
    for func in functions:
        thread = threading.Thread(target=func)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    mult_time = elapsed_time
    
    # print(f"Total time taken with multithreading: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main_sequential()
    # main_multithreaded()
    print(f"Total time taken to sequentially execute all functions: {seq_time:.2f} seconds")
    print(f"Total time taken with multithreading: {mult_time:.2f} seconds")

# Convert this whole code into a class. You dont need to include the sequential processing, just the multithreading will do. Each of the functions should remain the same as they have very specific conditions. Make seperate functions for each componenent and then a function called scrape_all() to scrape using multiple threads!