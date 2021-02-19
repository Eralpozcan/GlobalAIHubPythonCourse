# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 04:08:41 2021

@author: ASUS - Eralp ÖZCAN
"""

for i in range(3,1000):
    
    
    def prime_first(i):
        bolundu = False
        for j in range(2,i):
                if i % j == 0:
                    bolundu=True
                    # break yok...
        if bolundu == False:
            print("Birinci Fonksiyondan",i)
    
    def prime_second(i):
        bolundu = False
        for j in range(2,i):
            if i % j == 0:
                bolundu=True
                # break yok...
        if bolundu == False:
            print("İkinci Fonksiyondan",i)
    
    
    
    if i < 500 :
        prime_first(i)
    
    else:
        prime_second(i)