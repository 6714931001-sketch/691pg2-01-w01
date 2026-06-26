class Student:
    def __init__(self, Studentid, Studentfname, Studentlname, Studentdept):
        self.Studentid = Studentid    
        self.Studentfname = Studentfname
        self.Studentlname = Studentlname  
        self.Studentdept = Studentdept
    def __str__(self) -> str:
        return f"{self.Studentid} ,{self.Studentfname},{self.Studentlname},{self.Studentdept}"