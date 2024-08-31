# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:49:57 2024

@author: VoHuyHoang
"""
gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
giay = int(input("Nhập số giây: "))
a = f"{gio}h {phut}p {giay}s"
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print ("Kết quả là: ", a)
else:
    print("không hợp lệ")