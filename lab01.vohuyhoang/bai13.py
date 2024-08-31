# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:38:53 2024

@author: VoHuyHoang
"""
ngay = int(input("Nhập số ngày: "))
thang = int(input("Nhập số tháng: "))
nam = int(input("Nhập số năm: "))
# a 
a = f"{ngay}/{thang}/{nam}"
print("a. Định dạng: ")
print("ngày/tháng/năm: ",a)
# b 
short_years = nam % 100
b = f"{ngay}/{thang}/{short_years}"
print("b. Định dạng: ")
print("ngày/tháng/năm: ", b)
# c 
c = f"{nam}/{thang}/{ngay}"
print("c. Định dạng: ")
print("năm/tháng/ngày: ", c)
#Ngược lại
print("---------------------------")
print("Ngược lại")
# a 
a = f"{nam}/{thang}/{ngay}"
print("a. Định dạng: ")
print("năm/tháng/ngày: ", a)
# b 
short_years = nam % 100
b = f"{short_years}/{thang}/{ngay}"
print("b. Định dạng: ")
print("năm/tháng/ngày: ", b)
# c 
c = f"{ngay}/{thang}/{nam}"
print("c. Định dạng: ")
print("ngày/tháng/năm: ",c)


 
 

