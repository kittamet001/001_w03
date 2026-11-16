class Student: 
    def __init__ (self,sid,fullname,room):
        self.sid = sid
        self.fullname = fullname
        self.room = room
        
    def __str__ (self):
        return f"{self.sid}: {self.fullname} | {self.room}"