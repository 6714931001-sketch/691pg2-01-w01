class Building:
    def __init__(self,building,buname):
        self.building = building
        self.buname = buname
    def __str__(self) -> str:
        return f"{self.building} ,{self.buname}"