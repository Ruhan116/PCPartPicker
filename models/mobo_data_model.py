class moboModel:
    name : str
    size : str
    socket : str
    chipset : str
    
    def __init__(self, name, size, socket, chipset):
        self.name = name
        self.size = size
        self.socket = socket
        self.chipset = chipset