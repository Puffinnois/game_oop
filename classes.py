import numpy as np
import random

class Hero(): 
    
    positions = np.zeros((10,10))
    
    def __init__(self, name, xpos, ypos, hp = 100, atk = 5, dfs = 2, matk = 0, mdfs  = 0,  spd = 5, rge = 1, critFactor = 0, critRate = 0, movement = 5, items = {}):
        self.alive = True
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.atk = atk
        self.dfs = dfs
        self.matk = matk
        self.mdfs = mdfs
        self.spd = spd
        self.rge = rge
        self.critFactor = critFactor
        self.critRate = critRate
        self.xpos = xpos
        self.ypos = ypos
        self.movement = movement
        self.items = items
            
    def getHp(self):
        print(f"{self.name}'s hp : {self.hp}")
              
    def getPos(self):
        print(f"Position of {self.name} : {self.xpos},{self.ypos}")
        
    def getItems(self):
        print(f"Items of {self.name}: ")
        for i,y in self.items.items():
            print(f"Number of {i}: {y}")
              
    def move(self, x, y):
        if  x + y <= self.movement:
            self.xpos = self.xpos + x 
            self.ypos = self.ypos + y
            self.getPos()
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
            
class FightingWireFrames(Hero):
    def __init__(self, name, xpos, ypos, hp = 10, atk = 20, dfs = 0, matk = 0, mdfs  = 0,  spd = 1, rge = 1, critFactor = 0, critRate = 0, movement = 1, items = {} ):
        super().__init__(name, xpos, ypos, hp, atk, dfs, matk, mdfs, spd, rge, critFactor, critRate, movement, items)
           

    
   
    
