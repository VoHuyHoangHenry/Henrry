# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:51:46 2024

@author: VoHuyHoang
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
if a <= 0 or b <= 0:
    print("2 số phải là số nguyên dương")
else:
    #chia_lay_du
    d = a % b 
    #chia_lay_nguyen
    n = a // b 
print("Kết quả chia lấy dư là = ", d)
print("Kết quả chia lấy nguyên là = ", n)