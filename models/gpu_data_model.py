class gpuModel:
    name : str
    series : str
    vram : str
    tdp: str
    
    def __init__(self, name, series, vram, tdp) -> None:
        self.name = name
        self.series = series
        self.vram = vram
        self.tdp = tdp