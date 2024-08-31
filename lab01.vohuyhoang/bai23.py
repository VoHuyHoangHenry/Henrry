# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:46:26 2024

@author: VoHuyHoang
"""
import math 
a =float(input("Nhập hệ số a:"))
b =float(input("Nhập hệ số b:"))
c =float(input("Nhập hệ số c:"))
d = b*b -4*a*c
if  d == 0:
    x= -b/2*a
    print("Phương trình có nghiệm kép x= ", x )
elif d > 0: 
    x1= (-b +  math.sqrt(d))/(2*a)
    x2= (-b -  math.sqrt(d))/(2*a)
    print("Phương trình có 2 nghiệm phân biệt", x1, x2)
else:
    print("Phương trình vô nghiệm")
