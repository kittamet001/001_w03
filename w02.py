from Lecturer import Lecturer
from Subject import Subject
from student import Student
from room import Room
from build import Building

l01 = Lecturer("Ms.pumipat ounban")
r438 = Room("438")
r436 = Room("436")
r434 = Room("434")
r35408 = Room("35408")

s01 = Student("684931001", "kittamet boonlue", r438)

b4 = Building("4")
b35 = Building("35")
b4.addRoom(r438)
b4.addRoom(r436)
b4.addRoom(r434)
b35.addRoom(r35408)

Su1 = Subject("0943042-55", "standards in geoinformatics", "3")
Su2 = Subject("9042051-55", "Object oriented programming", "3")
Su3 = Subject("9043041-59", "Spatial Analysis and modeling", "3")
Su4 = Subject("0265011-65", "Digital Literacy for innovator", "3")
Su5 = Subject("9042052-59", "Advanced programming", "3")
Su6 = Subject("9042041-55", "Database Management in Geographic Information Systems", "3")

buildings = [b4, b35]
buildingCode = input("Building Code: ").strip()
selectedBuilding = next(
    (building for building in buildings if building.buildingCode == buildingCode),
    None,
)

if selectedBuilding:
    print(f"Rooms in Building {selectedBuilding.buildingCode}:")
    selectedBuilding.listRooms()
else:
    print("Building not found.")