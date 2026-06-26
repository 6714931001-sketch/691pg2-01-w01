class Lecturer:
    def __init__(self, lecrank, lecfname, leclname, lecdept):
        self.lecrank = lecrank    
        self.lecfname = lecfname  
        self.leclname = leclname  
        self.lecdept = lecdept
    def __str__(self) -> str:
        return f"{self.lecrank} ,{self.lecfname},{self.leclname},{self.lecdept}"