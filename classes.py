import numpy as np
import random

class Unit(): 
    
    positions = np.zeros((10,10))
    
    def __init__(self, name, xpos, ypos, hp = 100, mana = 0, atk = 5, dfs = 2, matk = 0, mdfs  = 0,  spd = 5, rge = 1, critFactor = 0, critRate = 0, movement = 5, items = {}):
        self.alive = True
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.mana = mana
        self.atk = atk
        self.dfs = dfs
        self.matk = matk
        self.mdfs = mdfs
        self.spd = spd
        self.rge = rge
        self.critFactor = critFactor
        self.critRate = critRate
        self.xpos, self.ypos = self._choosePosition(xpos, ypos)
        self.movement = movement
        self.items = items
        

    # todo
    def __choosePosition(self, x_wanted, y_wanted):
        if x_wanted >= 10 :
            x_wanted = 9
        if x_wanted < 0 :
            x_wanted = 0
        if y_wanted >= 10 :
            y_wanted = 9
        if y_wanted < 0 :
            y_wanted = 0
            
        while Unit.positions[x_wanted, y_wanted] == True :
            c = random.randint(0,2)
            if c == 0:
                if x_wanted > 5:
                    x_wanted -= 1
                if x_wanted <= 5:
                    x_wanted += 1
            if c == 1:
                if y_wanted > 5:
                    y_wanted -= 1
                if y_wanted <= 5:
                    y_wanted += 1

        Unit.positions[x_wanted, y_wanted] = True

        return x_wanted, y_wanted   
            

    def getHp(self):
        print(f"{self.name}'s hp : {self.hp}")
              
    def getPos(self):
        print(f"Position of {self.name} : {self.xpos},{self.ypos}")
        
    def getItems(self):
        print(f"Items of {self.name}: ")
        for i,y in self.items.items():
            print(f"Number of {i}: {y}")
              
    def move(self, x, y):
        if abs(x) + abs(y) <= self.movement:
            x_wanted = self.xpos + x 
            y_wanted = self.ypos + y
            if x_wanted > 0 and x_wanted < 10 and y_wanted > 0 and y_wanted < 10:
                if Unit.positions[x_wanted, y_wanted] == False:
                    Unit.positions[self.xpos, self.ypos] = False
                    Unit.positions[x_wanted, y_wanted] = True
                    self.movement = self.movement - (x + y)
                    self.xpos = x_wanted  
                    self.ypos = y_wanted
                    self.getPos()
                else:
                    print("you are trying to step on another unit")
            else:
                print("deserter !")
        else:
            print("not enough movement")
            
            
    def attack(self, enemy):
        if self.xpos - self.rge <= enemy.xpos and enemy.xpos <= self.xpos +  self.rge and self.ypos - self.rge <= enemy.ypos and  enemy.ypos <= self.ypos +  self.rge:
            if self.atk >= enemy.dfs:
                dmg = self.atk - enemy.dfs
                enemy.hp = enemy.hp - dmg
                print(f"You hit for {dmg} ")
                enemy.getHp()
                if enemy.hp <= 0:
                    enemy.alive = False
                    print(f"{enemy.name} has perished")
                self.movement = 0
            else:
                print("enemy defense is too high for you, you suck")
        else:
            print("enemy not in range")
    
    
    def usePotion(self):
        if self.items["potions"] >= 1:
            self.hp = self.hp + 10 if self.hp + 10 <= self.maxhp else self.maxhp
            self.getHp()
            self.items["potions"] -= 1 
        else:
            print("No potions left")

class Hero(Unit):
    def __init__(self, name, xpos, ypos, hp = 100, mana = 10, atk = 20, dfs = 0, matk = 0, mdfs  = 0,  spd = 1, rge = 1, critFactor = 0, critRate = 0, movement = 1, tpmovement = 5, items = {} ):
        super().__init__(name, xpos, ypos, hp, mana, atk, dfs, matk, mdfs, spd, rge, critFactor, critRate, movement, items)
        self.tpmovement = tpmovement

    def teleport(self, x, y):
        if self.mana > 5:
            if  x + y <= self.tpmovement:
                x_wanted = self.xpos + x 
                y_wanted = self.ypos + y
                if Unit.positions[x_wanted, y_wanted] == False:
                    Unit.positions[self.xpos, self.ypos] = False
                    Unit.positions[x_wanted, y_wanted] = True
                    self.tpmovement = self.tpmovement - (x + y)
                    self.mana = self.mana - 5
                    self.xpos = x_wanted  
                    self.ypos = y_wanted
                    self.getPos()
                else:
                    print("you are trying to teleport on another unit")

            else:
                print("not enough movement")
        else:
            print("not enough mana")


class FightingWireFrames(Unit):
    def __init__(self, name, xpos, ypos, hp = 10, mana = 0, atk = 20, dfs = 0, matk = 0, mdfs  = 0,  spd = 1, rge = 1, critFactor = 0, critRate = 0, movement = 1, items = {} ):
        super().__init__(name, xpos, ypos, hp, mana, atk, dfs, matk, mdfs, spd, rge, critFactor, critRate, movement, items)
           

    
   
    
