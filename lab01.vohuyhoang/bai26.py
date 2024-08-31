# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:17:15 2024

@author: VoHuyHoang
"""
#Câu a: 
print("Cau a: ")
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))

if a > b:
    a, b = b, a

if b > c:
    b, c = c, b

if a > b:
    a, b = b, a

print(f"Các số theo thứ tự tăng dần là: {a}, {b}, {c}")
#Câu b:
print("-----------------------------")
print("Cau b: ")
n = input("Nhập số nguyên n: ")
danh_sach = list(n)
danh_sach.sort()
ket_qua = ''.join (danh_sach)
print("Thứ tự tăng dần là: ", ket_qua)

