class Building:
    def __init__(self,buildingCode):
        self._buildingCode = buildingCode
        self._rooms = []
    def __str__(self):
        return f"Building : {self._buildingCode}"


    @property
    def buildingCode(self):
        return self._buildingCode
    @buildingCode.setter
    def buildingCode(self,value):
        self._buildingCode = value


    def addRoom(self,room):
        self._rooms.append(room)

    def findRoom(self,roomCode):
        for room in self._rooms:
            if room.roomcode == roomCode:
                return room
        return None

    def listRooms(self):
        for room in self._rooms :
           print(room.roomcode)
