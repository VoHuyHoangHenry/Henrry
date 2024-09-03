# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:37:00 2024

@author: ADMIN
"""

so_xe = float(input("Nhập số xe gồm 4 chữ số: "))
a = so_xe // 1000
b = so_xe % 1000
c = b // 100
d = b % 100
e = d // 10
f = d % 10
tong = a + c + e + f

if  0 <= tong <= 9:
    print("Số nút là: ", tong)
else:
    so_dau = tong // 10
    so_cuoi = tong % 10
    ket_qua = so_dau + so_cuoi
    print("Số nút là: ", ket_qua)
              