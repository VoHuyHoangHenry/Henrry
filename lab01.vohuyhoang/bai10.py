# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:49:55 2024

@author: VoHuyHoang
"""
so_xe = float(input("Nhập số xe gồm 4 chữ số: "))
a = so_xe // 1000
b = so_xe % 1000
c = b // 100
d = b % 100
e = d // 10
f = d % 10
tong = a + c + e + f

if 1000 <= so_xe <= 9999:
    print("Số nút là: ", tong)
else:
    print("Vui lòng nhập 4 chữ số") 
              
