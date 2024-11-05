class ramModel:
    name : str
    size : str
    type : str
    bus_speed : str 
    quantity : str
    
    def __init__(self, name, size, type, bus_speed, quantity):  # <--- This is the constructor
        self.name = name
        self.size = size
        self.type = type
        self.bus_speed = bus_speed
        self.quantity = quantity