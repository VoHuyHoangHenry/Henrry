# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:41:25 2024

@author: VoHuyHoang
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c
print ("Số lớn nhất là: ", so_lon_nhat)
