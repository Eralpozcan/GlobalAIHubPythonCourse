# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:35:28 2021

@author: ASUS
"""




class Cooks():
    def __init__(self,name):
        self.name =name
        
        
    def cooking(self):
        
        print("Cook ready! ")
        

class Pasta(Cooks):
    def __init__(self,name,water,oil,salt,pasta):
        super().__init__(name)
        self.water = water
        self.oil = oil
        self.salt = salt
        self.pasta = pasta
        
    def proses(self):
        print("First Section "+self.water+"")
        print("Then water is boiled **Waiting ten minutes")
        print("İf water is boiled,Add "+self.pasta+" ")
        print("Section 3 : add "+self.salt+"")
        print("If the pasta gets the desired hardness we add "+self.oil+"")
        print("Section finally")
        

        
class Meat(Cooks):
    def __init__(self,name,meat,oil,salt,thyme):
        super().__init__(name)
        self.name =name
        self.meat =meat
        self.oil =oil
        self.salt = salt
        self.thyme = thyme
        
    def prosess(self):
        print("We add :"+self.oil+" in pad.")
        print("We add "+self.meat+" in pad and "+self.salt+","+self.thyme+"")
        print("If it's cooked, visit the stove.")
        
        
class Pizza(Cooks):
    def __init__(self,name,cheese,sauce,sausage):
        super().__init__(name)
        self.name = name
        self.cheese = cheese
        self.sauce= sauce
        self.sausage = sausage
        
    def proses(self):
        print("We buy dought. And roll dought")
        print("We add : "+self.sauce+" in rolled dought")
        print("We add  "+self.cheese+" in dought and "+self.sausage+"")
        print("Then give to oven")
        
        
        
choose = input("Choose a cooking 1- Pasta,2 -Meat,3-Pizza \n Select your chose :")

if(choose == "1"):
        cName = input("Give pasta name:")
        cWater = input("Enter the Water amount :")
        cOil = input("Enter the oil amount :")
        cSalt = input("Enter the salt amount:")
        cPastaType = input("Enter the pasta type(fusilli,spaghettini etc.) :")
        
        cPros = Pasta(cName,cWater,cOil,cSalt,cPastaType)
        cPros.proses()
        cPros.cooking()
        
elif(choose =="2"):
        cName = input("Give meat name:")
        cMeat = input("Enter the Meat amount :")
        cOil = input("Enter the oil amount :")
        cSalt = input("Enter the salt amount:")
        cThyme = input("Enter the thyme (other spice) amount :")
        
        cMeat =Meat(cName,cWater,cOil,cSalt,cThyme)
        cMeat.proses()
        cMeat.cooking()
elif(choose =="3"):
        cName = input("Give pasta name:")
        cCheese = input("Enter the Water amount :")
        cSauce = input("Enter the oil amount :")
        cSausage = input("Enter the salt amount:")
        
        cPizza =Pizza(cName,cCheese,cSauce,cSausage)
        cPizza.proses()
        cPizza.cooking()
else:
         print("Please check your selection!")
