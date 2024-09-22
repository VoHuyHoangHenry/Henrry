# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:01:14 2024

@author: VoHuyHoang
"""

n = int(input("Nhập vào số nguyên n: "))
while n <= 0:
    n = int(input("Không đủ điều kiện vui lòng nhập lại số nguyên duong: "))
tong = 1
for i in range ( 1, n+ 1):
    tong *= i
print("S= ", tong)

