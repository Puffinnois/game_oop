def createMapCell():
    obstacle = False
    items = {}
    if random.randint(0,100) < 10:
        obstacle = True
    if random.randint(0, 100) < 2:
        items["potions"] = 1
    return MapCell(player = False, obstacle = obstacle, items = items)
    

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

    
        
    
