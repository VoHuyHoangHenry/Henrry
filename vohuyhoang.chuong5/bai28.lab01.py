# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:18:44 2024

@author: VoHuyHoang
"""

n = int(input("Nhập vào số nguyên dương N: "))
while n < 0:
    n = int(input("Nhập lại số nguyên dương N: "))
so = []
for i in range(1, n + 1):
    if n % i == 0:
        so += [i]
print(f"Uớc số của {n} là: ", so)