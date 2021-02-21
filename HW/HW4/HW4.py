# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 18:30:44 2021

@author: ASUS

Base of GeekforGeeks :
https://www.geeksforgeeks.org/python-program-for-word-guessing-game/

"""


import random as rnd


name = input("Adınız nedir? ")

print("İyi şanslar", name)


class Hangman:
    
    
    def __init__(self,char):
        self.char = char
        
        
    def game(self):
        
        word = ['rainbow', 'computer', 'science', 'programming', 
         'python']
        
        secretword = rnd.choice(word)
        self.char = input("Tahmininniz :")
        
        guess = ''
        
        turns = len(secretword)
        
        while turns > 0:
            failed = 0
            for self.char in secretword:
                if self.char in guess:
                    print(self.char)
                else:
                    print("_")
                    failed +=1
            
            if failed == 0:
                print("Tebrikler")
                print("The secret word:",secretword)
            
            tahmin= input("Your input:")
            guess +=tahmin
            
            if tahmin not in secretword:
                
                turns  -= 1
                print("Wrong")
                print("You have", + turns, 'more guesses')
             
             
                if turns == 0:
                    print("You Loose")
                    
        
start = Hangman("")
start.game()