class Room:
    def __init__(self,roomCode):
        self._roomCode = roomCode
    def __str__(self):
        return f"room : {self._roomCode}"
    
    @property
    def roomcode(self):
        return self._roomCode
    @roomcode.setter
    def roomcode(self,value):
        self._roomCode = value