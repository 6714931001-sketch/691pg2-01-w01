class CM :
    def __init__(self,place,ground,distance,distanceType,direction,season,weather,groundCondition):
            self.place = place
            self.ground = ground
            self.distance = distance
            self.distanceType = distanceType
            self.direction = direction
            self.season = season
            self.weather = weather  
            self.groundCondition = groundCondition
    def __str__(self) -> str:
        return f"{self.place} {self.ground} {self.distance} {self.distanceType} {self.direction} {self.season} {self.weather} {self.groundCondition}"
