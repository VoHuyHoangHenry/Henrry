# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:44:56 2024

@author: VoHuyHoang
"""
km = int (input("Số quãng đường đã đi (km): "))
km_dau = 15
km_hai = 13.5
km_ba = 11
giam_gia = 0.90
tong = 0
for i in range(1, 1 + km):
    if i == 1:
        tong = tong + km_dau
    elif 2 <=  i <= 5:
        tong = tong + km_hai
    elif i >= 6:
        tong = tong + km_ba
    if i > 120:
        tong = tong*0.90 
print("Tổng số tiền đã đi: ", tong)