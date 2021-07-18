import random

class Map():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = self.createMap()
    
    def createMap(self):
        map = []

        for i in range(self.height):
            map.append([])
            for j in range(self.width):
                map[i].append(createMapCell())
        return map

class MapCell():
    def __init__(self, player, obstacle, landType = 0, items = {}):
        self.player = player
        self.obstacle = obstacle
        self.landType = landType
        self.items = items
    
def createMapCell():
    obstacle = False
    items = {}
    if random.randint(0,100) < 10:
        obstacle = True
    if random.randint(0, 100) < 2:
        items["potions"] = 1
    return MapCell(player = None, obstacle = obstacle, items = items)

def chooseMapSize():
    print("list of different map size:\n- small: 1\n- medium: 2\n- big: 3")
    choice = False
    a = input("map choice: ")
    while type(choice) is not int or choice < 1 or choice > 3:
        try:
            choice = int(a)
            assert choice >= 1 
            assert choice <= 3 
        except:
            a = input("Integer needed and between 1 and 3, enter the number again: ")

    if choice == 1:
       map = Map(height = 5, width = 5)

    if choice == 2:
       map = Map(height = 10, width = 10)

    if choice == 3:
       map = Map(height = 25, width = 25)

    return map
        
gameMap = chooseMapSize()    
