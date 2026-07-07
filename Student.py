from Program import Program

class Student:
    def __init__(self, Studentid, Studentfname, Studentlname, Studentdept: Program):
        self.Studentid = Studentid
        self.Studentfname = Studentfname
        self.Studentlname = Studentlname
        self.Studentdept = Studentdept

    def __str__(self):
        return f"รหัส {self.Studentid} {self.Studentfname} {self.Studentlname} - สาขา {self.Studentdept}"