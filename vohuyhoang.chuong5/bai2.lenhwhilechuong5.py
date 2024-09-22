# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:21:10 2024

@author: ADMIN
"""
a = float(input("Nhập giá trị (phải là số thực) từ {-89.9 - 88.8}: "))
while -89.9 <= a <= 88.8:
    print("Thõa điều kiện")
    break 
else:
    print("Bạn không thỏa điều kiện")
    b = float(input("Vui lòng nhập lại: "))
    print("Bạn đã thỏa điều kiện")

