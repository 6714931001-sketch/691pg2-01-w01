from Building import Building
class Room :
    def __init__(self,rid,rname,building):
        self.rid = rid
        self.rname = rname
        self.building = building
    def __str__(self):
         return f"ห้อง{self.rid} วิชา{self.rname} {self.building.getBuildingName()}"