# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:21:54 2024

@author: VoHuyHoang
"""
n = int(input("Nhập vào số nguyên n: "))
while n <= 0:
    n = int(input("Không đủ điều kiện vui lòng nhập lại số nguyên duong: "))
tong = 0
for i in range ( 0, n + 1):
    tong += ((2*n) + 1)/((2*n) + 2)
print("S= ", tong)
