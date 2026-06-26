class Room:
    def __init__(self,Room,Roomname):
        self.Room = Room
        self.Roomname = Roomname
    def __str__(self) -> str:
        return f"{self.Room} ,{self.Roomname}"