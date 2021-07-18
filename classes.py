import numpy as np
import random
from map import gameMap

class Unit(): 
    
    unit_counter = 0

    def __init__(self, name, xpos, ypos, expvalue = 10, hp = 100, mana = 0, atk = 5, dfs = 2, matk = 0, mdfs  = 0,  spd = 5, rge = 1, critFactor = 0, critRate = 0, movement = 5, items = {}):
        self.alive = True
        self.name = name
        self.expvalue = expvalue
        self.hp = hp
        self.hp_max = hp
        self.mana = mana
        self.mana_max = mana
        self.atk = atk
        self.dfs = dfs
        self.matk = matk
        self.mdfs = mdfs
        self.spd = spd
        self.rge = rge
        self.critFactor = critFactor
        self.critRate = critRate
        self.xpos, self.ypos = self.__choosePosition(xpos, ypos)
        self.movement = movement
        self.movement_max = movement
        self.items = items
        self.id = Unit.unit_counter + 1
        Unit.unit_counter += 1
    
    def __death(self):
        self.alive = False
        print(f"{self.name} has perished")
        Unit.positions[self.xpos, self.ypos] = False

    def __choosePosition(self, x_wanted, y_wanted):
        if x_wanted >= gameMap.height :
            x_wanted = gameMap.height - 1
        if x_wanted < 0 :
            x_wanted = 0
        if y_wanted >= gameMap.width :
            y_wanted = gameMap.width - 1
        if y_wanted < 0 :
            y_wanted = 0
            
        while gameMap.map[x_wanted][y_wanted].player != None or gameMap.map[x_wanted][y_wanted].obstacle == True:
            
            c = random.randint(0,2)
            if c == 0:
                x_temp = x_wanted
                if x_temp > gameMap.height / 2:
                    x_wanted -= 1
                if x_temp <= gameMap.height / 2:
                    x_wanted += 1
            if c == 1:
                y_temp = y_wanted
                if y_temp > gameMap.width / 2:
                    y_wanted -= 1
                if y_temp <= gameMap.width / 2:
                    y_wanted += 1

        gameMap.map[x_wanted][y_wanted].player = self

        return x_wanted, y_wanted   
            

    def __getHp(self):
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
                enemy.__getHp()
                if enemy.hp <= 0:
                    enemy.__death()
                self.movement = 0
            else:
                print("enemy defense is too high for you, you suck")
        else:
            print("enemy not in range")
    
    
    def usePotion(self):
        if self.items["potions"] >= 1:
            self.hp = self.hp + 10 if self.hp + 10 <= self.hp_max else self.hp_max
            self.__getHp()
            self.items["potions"] -= 1 
        else:
            print("No potions left")

class Hero(Unit):
    def __init__(self, name, xpos, ypos, lvl = 1, exp = 0, exptolvlup = 100, expvalue = 50, hp = 100, mana = 10, atk = 20, dfs = 0, matk = 0, mdfs  = 0,  spd = 1, rge = 1, critFactor = 0, critRate = 0, movement = 1, tpmovement = 5, items = {} ):
        super().__init__(name, xpos, ypos, expvalue, hp, mana, atk, dfs, matk, mdfs, spd, rge, critFactor, critRate, movement, items)
        self.lvl = lvl
        self.exp = exp
        self.exptolvlup = exptolvlup
        self.tpmovement = tpmovement
        self.tpmovement_max = tpmovement
        
    
    def showStats(self):
        print(f"{self.name}: {self.exp}/{self.exptolvlup} xp\n{self.hp} hp\n{self.mana} mana\n{self.atk} atk\n{self.dfs} dfs")

    def __lvlup(self):
        self.lvl += 1
        self.exp = self.exp - self.exptolvlup
        self.exptolvlup += 5
        self.expvalue += 5
        self.hp_max += 10
        self.hp = self.hp_max    
        self.mana += 5
        self.mana = self.mana_max
        self.atk += 2
        self.dfs += 1
        print(f"{self.name} has leveled up and is now level {self.lvl}")
        self.showStats()

    def __gainExp(self, expvalue):
        self.exp += expvalue
        if self.exp >= self.exptolvlup:
            self.__lvlup()
        else:
            print(f"{self.exp}/{self.exptolvlup} xp")

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

    def attack(self, enemy):
        super().attack(enemy)
        if enemy.alive == False:
            self.__gainExp(enemy.expvalue)

class Berserk(Unit):
    def __init__(self, name, xpos, ypos, expvalue = 50, hp = 75, mana = 0, atk = 10, dfs = 3, matk = 0, mdfs  = 0,  spd = 5, rge = 1, critFactor = 0, critRate = 0, movement = 5, items = {}, rage = 0):
        super().__init__(name, xpos, ypos, expvalue, hp, mana, atk, dfs, matk, mdfs, spd, rge, critFactor, critRate, movement, items)
        self.rage = rage
    
    def frenzy(self):
        if self.rage >= 20:
            self.atk += 10
            self.dfs = 0
            self.rage -= 20
            print(f"{self.name} is enraged !")
        else: 
            print(f"Not bloody enough for the gods ({self.rage}/20 rage)")

    def attack(self, enemy):
        super().attack(enemy)
        self.rage += 5
        print(f"you have {self.rage} rage") 

class Paladin(Unit):
    def __init__(self, name, xpos, ypos, expvalue = 50, hp = 75, mana = 0, atk = 10, dfs = 3, matk = 0, mdfs  = 0,  spd = 5, rge = 1, critFactor = 0, critRate = 0, movement = 5, holiness = 0, items = {}):
        super().__init__(name, xpos, ypos, expvalue, hp, mana, atk, dfs, matk, mdfs, spd, rge, critFactor, critRate, movement, items)
        self.holiness = holiness
    
    def sanctify(self, enemy):
        if self.holiness >= 3:
            self.atk += 25
            print("By the power of the gods !")
            super().attack(enemy)
            self.atk -= 25
            self.holiness -= 3
        else: 
            print(f"Not holy enough for the gods ({self.holiness}/3 holiness)")

    def attack(self, enemy):
        super().attack(enemy)
        if enemy.alive == False:
            self.holiness += 1
            print(f"you have {self.holiness} holiness") 
        
class FightingWireFrames(Unit):
    def __init__(self, name, xpos, ypos, expvalue = 15, hp = 10, mana = 0, atk = 20, dfs = 0, matk = 0, mdfs  = 0,  spd = 1, rge = 1, critFactor = 0, critRate = 0, movement = 1, items = {} ):
        super().__init__(name, xpos, ypos, expvalue, hp, mana, atk, dfs, matk, mdfs, spd, rge, critFactor, critRate, movement, items)
           

    
   
    
