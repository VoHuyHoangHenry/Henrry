# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:45:17 2024

@author: VoHuyHoang
"""
import math 
a = float  (input("Nhập hệ số a: "))
b = float  (input("Nhập hệ số b: "))
cong_thuc = (((a + b) / (math.pow(a, 1/3) + math.pow(b, 1/3))) - (math.pow((a*b), 1/3))) / math.pow((math.pow(a, 1/3)) - (math.pow(b, 1/3)), 2)

print ("Kết quả là = ", cong_thuc)


