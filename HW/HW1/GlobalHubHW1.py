#!/usr/bin/env python
# coding: utf-8

# Create a program will compute the tax and the tip for a meal ordered at a restaurant. You can compute the tax as 8 percent of the meal amount and the tip as 10 percent of the meal amount (without the tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal including both the tax and the tip.
# 
# a)Define the cost of the meal in the beginning of your program.
# 
# Some several example program runs:
# 
# Cost of the meal is 25 Eur.
# 
# Sample Run: The tax is 2.00 Eur and the tip is 2.50 Eur, making the total 29.50 Eur.
# 
# Cost of the meal is 68 Eur.
# 
# Sample Run: The tax is 5.44 Eur and the tip is 6.80000000000001 Eur, making the total 80.24 Eur.
# 
# b)Input the cost of the meal from the user.
# 
# Some several example program runs:
# 
# Please enter the cost of your meal: 100
# 
# Sample Run: The tax is 8.00 Eur and the tip is 10.00 Eur, making the total 118.00 Eur.
# 
# Please enter the cost of your meal: 68
# 
# Sample Run: The tax is 5.44 Eur and the tip is 6.80 Eur, making the total 80.24 Eur.
# 
# 

# In[1]:


mealprice =int(input("Yemek ücretini giriniz:"))


taxrate = 8
tipsrate = 10


# In[2]:


def tax(mealprice):
    return mealprice * taxrate/100
def tips(mealprice):
    return mealprice * (tipsrate/100)

def calculator(mealprice,tax,tips):

    return mealprice + tax + tips


# In[3]:


tax = tax(mealprice)
tips = tips(mealprice)
result = calculator(mealprice,tax,tips)


# In[4]:


print(result)


# In[11]:


print("Vergi tutarı :"+format(tax)+"$ ,bahşiş tutarınız :"+format(tips)+" $ toplam yemek ücretiniz:"+format(result)+"$")


# In[ ]:




