# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:05:29 2024

@author: ADMIN
"""

x = float(input("Nhập giá trị: "))
while -99 <= x <= 99:
    print("Thõa điều kiện")
    break 
else:
    print("Bạn không thỏa điều kiện")
    b = float(input("Vui lòng nhập lại: "))
    print("Bạn đã thỏa điều kiện")

