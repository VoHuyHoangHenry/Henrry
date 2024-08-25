# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:30:54 2024

@author: vohuyhoang
"""
g = float(input("Nhập giờ: "))
p = float(input("Nhập phút: "))
s = float(input("Nhập giây: "))
tong_so_giay = (g * 3600) + (p * 60) + s
print("Tổng số giây là= ", tong_so_giay)
