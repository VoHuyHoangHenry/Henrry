# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:32:07 2024

@author: VoHuyHoang
"""
#Thời gian thứ 1
gio_1 = int(input("Nhập số giờ thứ 1: "))
phut_1 = int(input("Nhập số phút thứ 1: "))
giay_1 = int(input("Nhập số giây thứ 1: "))
a = f"{gio_1}h {phut_1}p {giay_1}s"
print("Thời gian thứ nhất: ", a)
print("==============================")
#Thời gian thứ 2
gio_2 = int(input("Nhập số giờ thứ 2: "))
phut_2 = int(input("Nhập số phút thứ 2: "))
giay_2 = int(input("Nhập số giây thứ 2: "))
b = f"{gio_2}g, {phut_2}p, {giay_2}s"
print("Thời gian thứ hai: ", b)
#Tổng
print("------------------------------")
gio_c = gio_1 + gio_2
phut_c = phut_1 + phut_2
giay_c = giay_1 + giay_2
tong_time = f"{gio_c}h, {phut_c}p, {giay_c}s"
print("Tổng 2 thời gian là: ", tong_time)
#Hiệu 
#th1
gio_h_1 = gio_1 - gio_2
phut_h_1 = phut_1 - phut_2
giay_h_1 = giay_1 - giay_2
hieu_time_1 = f"{gio_h_1}h, {phut_h_1}p, {giay_h_1}s"
#th2
gio_h_2 = gio_2 - gio_1
phut_h_2 = phut_2 - phut_1
giay_h_2 = giay_2 - giay_1
hieu_time_2 = f"{gio_h_2}h, {phut_h_2}p, {giay_h_2}s"

if gio_1 > gio_2 and phut_1 > phut_2 and giay_1 > giay_2:
     print("Hiệu 2 thời gian là: ", hieu_time_1)
elif gio_2 > gio_1 and phut_2 > phut_1 and giay_2 > giay_1:
     print("Hiệu 2 thời gian là: ", hieu_time_2)
else:
    print(" Thời gian không hợp lệ")
