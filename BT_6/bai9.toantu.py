# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:34:39 2024

@author: ADMIN
"""

import math 
a =float(input("Nhập giá trị a: "))
b =float(input("Nhập giá trị b: "))  
c = ((math.pow(a, 1/2)-math.pow(b, 1/2))/(math.pow(a, 1/4)-math.pow(b, 1/4)))-((math.pow(a, 1/2)+math.pow(a*b, 1/4))/(math.pow(a, 1/4)+math.pow(b,1/4)))
print ("Kết quả là= ", c)