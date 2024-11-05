class hddModel:
    name : str
    size : str
    rpm : str
    
    def __init__(self, name, size, rpm):
        self.name = name
        self.size = size
        self.rpm = rpm