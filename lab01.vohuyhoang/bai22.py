# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:45:18 2024

@author: VoHuyHoang
"""
a=float (input("Nhập hệ số thứ nhất :"))
b=float (input("Nhập hệ số thứ hai :"))
if a == 0 and b == 0:
    print("Phương trình vô số nghiệm")
elif a != 0 and b == 0:
    print ("Phương trình vô nghiệm")
elif a ==0 and b != 0:
    print("Phương trình vô nghiệm")
else: 
    x=-b/a
    print ("Phương trình có nghiệm x= ",x)
