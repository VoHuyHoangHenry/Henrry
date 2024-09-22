# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 01:37:34 2024

@author: VoHuyHoang
"""
n = int(input("Nhập giá trị nguyên n: "))
b = {a: a ** a for a in range(1, n+1)}
print(b)
