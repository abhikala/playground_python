#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
#
print("\n********************************************************\n")
def check_prime(num):
    #print("check_prime num = ",num)
    if num <= 1:
        result = False
    else:
        result = True
        for i in range (2,num):
            if ((num % i) == 0):
                result = False
                break
    if result:
        print(num, "is a prime number.")
    else:
        print(num, "is NOT a prime number")
    return result
#
wantmore = True
while(wantmore):
    number = int(input('Enter a number: '))
    check_prime_response = check_prime(number)
    response = ''
    while(response !='y' and response !='n'):
        response = str(input("Want to check more numbers? [y/n]: "))
    if response == 'y' :
        wantmore = True
    elif response == 'n':
        wantmore = False
        print("\n..Exiting")
    else:
        print("\nERROR! ..Exiting")
        break
print("\n********************************************************\n")


# In[ ]:




