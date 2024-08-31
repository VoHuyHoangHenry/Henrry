# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:45:30 2024

@author: VoHuyHoang
"""

g = int (input("Nhập giờ: "))
p = int (input("Nhập phút: "))
s = int (input("Nhập giây: "))
a = f"{g}h {p}p {g}s"
print("In ra: ", a)
tong_so_giay = (g * 3600) + (p * 60) + s
print("Tổng số giây là: ", tong_so_giay)