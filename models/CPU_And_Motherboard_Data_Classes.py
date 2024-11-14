class CPU:
    def __init__(self, cpu_id, name, socket_type, cores, clock_speed, price):
        self.cpu_id = cpu_id
        self.name = name
        self.socket_type = socket_type
        self.cores = cores
        self.clock_speed = clock_speed
        self.price = price

    def __repr__(self):
        return f"{self.name} (Socket: {self.socket_type}, Price: {self.price})"


class Motherboard:
    def __init__(self, motherboard_id, name, socket_type, form_factor, ram_type, price):
        self.motherboard_id = motherboard_id
        self.name = name
        self.socket_type = socket_type
        self.form_factor = form_factor
        self.ram_type = ram_type
        self.price = price

    def __repr__(self):
        return f"{self.name} (Socket: {self.socket_type}, RAM Type: {self.ram_type}, Price: {self.price})"
