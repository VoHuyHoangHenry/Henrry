# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:44:11 2024

@author: VoHuyHoang
"""
n = int(input("Nhập vào số nguyên duong n: "))
while  n < 2:
    n = int(input("Số nguyên tố phải lớn hơn 2, vui lòng nhập lại: "))

for i in range(2, n):
     if n % i == 0:
        print("Không phải là số nguyên tố")
        break 
else:
    print(f"{n} là số nguyên tố")       