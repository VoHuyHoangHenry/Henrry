# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:56:19 2024

@author: VoHuyHoang
"""
import math 
hinh = input("Nhập hình: ")
if hinh == "v":
    print("Tính P và S của hình vuông")
    a = float(input("Nhập chiều dài các cạnh: "))
    dien_tich_hv =  a*a
    chu_vi_hv = a*4
    print ("Diện tích hình vuông là: ", dien_tich_hv)
    print("Chu vi hình vuông là: ", chu_vi_hv)
elif hinh == "n":
    print("Tính P và S của hình chữ nhật")
    b = float(input("Nhập chiều dài: "))
    c = float(input("Nhập chiều rộbg: "))
    dien_tich_hcn = b * c
    chu_vi_hcn = (b + c) * 2
    print ("Diện tích hình chữ nhật là: ", dien_tich_hcn)
    print("Chu vi hình chữ nhật là: ", chu_vi_hcn)
elif hinh == "t":
    print("Tính P và S của hình tròn")
    r = float(input("Nhập bán kính hình tròn: "))
    chu_vi_tron = 2 * math.pi * r
    dien_tich_tron = (chu_vi_tron**2) / 4 * math.pi 
    print ("Diện tích hình tròn là: ", dien_tich_tron)
    print("Chu vi hình tròn là: ", chu_vi_tron)
else:
    print("Không tìm thấy hình")
        
    
    
    
    
