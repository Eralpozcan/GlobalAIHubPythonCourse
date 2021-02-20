# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 03:25:35 2021

@author: ASUS
"""


namefirstname = []
studentnotelist = []
ortalamaliste = []
my_dict = {}


def ortalama_hesapla(midterm,final,homework):
    """Midterm %30
       Final %50
       Homework %20"""
    return midterm * 0.3 + final * 0.5 + homework * 0.2


def ortalamalist(ortalama):
    """Add list find averange point"""
    
    ortalamaliste.append(ortalama)
    #print(ortalamaliste)    
     

for i in range(6):
    if i <=4:
        name = input("Adını Giriniz :")
        lastname = input("Soyadını Giriniz:")
        midterm = int(input("Vize Sınavını Giriniz :"))
        final = int(input("Final Sınavını Giriniz :"))
        homework = int(input("Ödev Puanını giriniz :"))
        
        #Append list first name and lastname
        namefirstname.append(""+name + " "+ lastname+"")
        
        #Calculate average
        ortalama = ortalama_hesapla(midterm, final, homework)
        
        ortalamalist(ortalama)
        
        #Add student note list and average
        studentnotelist.append([midterm,final,homework,ortalama])
        
        #add dictionary : namefirstname(List) ,Value:studentnotelist(List)
        my_dict[namefirstname[i]] = studentnotelist[i]
        a = max(ortalamaliste)
        getIndex = ortalamaliste.index(a)
        
        #print("İndex", getIndex)
        print(my_dict)
    elif i>=5:
        print("Tebrikler {}".format(namefirstname[getIndex]))


    
    
    
    
    