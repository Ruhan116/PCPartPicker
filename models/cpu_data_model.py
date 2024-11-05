class cpuModel:
    name : str
    socket : str
    clock_speed : str
    cores : int
    threads : int
    
    def __init__(self, name, socket, clock_speed, cores, threads) -> None:
        self.name = name
        self.socket = socket
        self.clock_speed = clock_speed
        self.cores = cores
        self.threads = threads
