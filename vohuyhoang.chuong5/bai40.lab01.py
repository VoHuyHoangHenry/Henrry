# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:19:31 2024

@author: VoHuyHoang
"""
n = int(input("Nhập vào số nguyên n: "))
while n <= 0:
    n = int(input("Không đủ điều kiện vui lòng nhập lại số nguyên duong: "))
tong = 0
for i in range ( 1, n + 1):
    tong += 1/(2*i)
print("S= ", tong)

