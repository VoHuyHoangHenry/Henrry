# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:25:00 2024

@author: ADMIN
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
so_nho_nhat = a
if b < so_nho_nhat:
    so_nho_nhat = b
if c < so_nho_nhat:
    so_nho_nhat = c
if d < so_nho_nhat:
    so_nho_nhat = d
print ("Số nhỏ nhất là: ", so_nho_nhat)
