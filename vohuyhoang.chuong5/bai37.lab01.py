# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 23:54:08 2024

@author: VoHuyHoang
"""
n = int(input("Nhập vào số nguyên n: "))
while n <= 0:
    n = int(input("Không đủ điều kiện vui lòng nhập lại số nguyên duong: "))
tong = 0
for i in range ( 0, n+ 1, 2):
    tong += i
print("S= ", tong)


