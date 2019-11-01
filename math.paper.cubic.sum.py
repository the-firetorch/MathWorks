# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:59:37 2019

@author: 91902
"""


x=0
y=0
z=0
sum=0
for i in[0,10]:
    for j in[0,10]:
        for k in[0,10]:
            sum=x**3 +y**3+z**3
            if sum==3:
                print("success")
                print(x,y,z)
                
            z+=1
        
        y+=1
        z=0
        
    x+=1
    y=0
    z=0
    
    

        
            
            