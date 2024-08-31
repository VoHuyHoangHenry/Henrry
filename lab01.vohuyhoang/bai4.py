# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:08:57 2024

@author: VoHuyHoang
"""
a = int(input("Nhập số nguyên dương có 2 chữ số: "))
if 10 <= a <= 99:
    so_dau = a // 10
    so_cuoi = a % 10
    tong = (so_dau) + (so_cuoi)
    print("Kết quả là: ", tong)
else:
    print("Vui lòng nhập số nguyên dương có 2 chữ số")
        