class Building:
    def __init__(self,buid,buname):
        self.buid = buid
        self.buname = buname
    def __str__(self):
        return f"อาคาร {self.buid}"
    def getBuildingName(self) :
        return f"{self.buname}"
    def setBuildingName(self,name) :
        self.buname = name
