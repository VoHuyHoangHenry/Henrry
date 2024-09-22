# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 00:21:57 2024

@author: VoHuyHoang
"""
n = int(input("Nhập vào số n: "))
x = int(input("Nhập vào số x: "))

while n <= 0:
    n = int(input("Không đủ điều kiện, vui lòng nhập lại số nguyên dương: "))

tong_tu = 0
tong_mau = 0
#tính tổng 
for i in range(1, n + 1):
    tong_mau += i
# Tính tổng tử
for a in range(0, x + 1):
    tong_tu += (a ** n)  # Cộng dồn a^n vào tong_tu
# Tính S
if tong_mau != 0:  # Kiểm tra tránh chia cho 0
    S = tong_tu / tong_mau
else:
    S = 0

print("S =", S)
