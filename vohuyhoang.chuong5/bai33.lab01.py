# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:17:31 2024

@author: VoHuyHoang
"""
import math 
n = int(input("Nhập vào số nguyên duong n: "))
a = math.sqrt(n) 
while int(a) != a:
    n = int(input("Đây không phải là số chính phương"))
else:
    print(f"{n} lá số chính phương")
    
