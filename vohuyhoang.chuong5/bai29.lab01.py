# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:43:19 2024

@author: VoHuyHoang
"""
n = int(input("Nhập số nguyên N: "))
while n < 0:
    n = int(input("Vui lòng nhập lại số nguyên N: "))
tong = 0
for i in str(n):
    tong += int(i)
print(f"tổng của số nguyên {n} là: ", tong)