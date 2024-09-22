# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:28:33 2024

@author: VoHuyHoang
"""
nhap_thang_nam = input("Nhập tháng và năm theo định dạng tháng/năm: ")
thang, nam = nhap_thang_nam.split("/")
thang = int(thang)
nam = int(nam)
nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
cac_ngay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if nam_nhuan:
    cac_ngay[1] = 29
for i in range(1, 13):
    if i == thang:
        print(f"Thang {thang} nam {nam} có {cac_ngay[i-1]} ngay")
    
    