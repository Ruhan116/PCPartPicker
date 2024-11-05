class ssdModel:
    name : str
    size : str
    bus : str
    format : str
    
    def __init__(self, name, size, bus, format):
        self.name = name
        self.size = size
        self.bus = bus
        self.format = format