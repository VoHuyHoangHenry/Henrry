# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:11:37 2024

@author:VoHuyHoang
"""
print("Nhập 3 kích thước xem có phải tam giác không?")
a =float(input("Nhập hệ số a: "))
b =float(input("Nhập hệ số b: "))
c =float(input("Nhập hệ số c: "))
while a > 0 and b > 0 and c > 0:
    if a + b > c or a + c > b and b + c > a:
        print("Hệ số a, b, c tạo thành tam giác")
        if a==b==c:
            print ("Đây là tam giác đều.")
            break 
        elif a==b or a==c or b==c:
            print ("Đây là tam giác cân.")
            break 
        elif a**2== b**2 + c**2 or b**2 == a**2 + c**2 or c**2== b**2 + a**2:
            print ("Đây là tam giác vuông.")
            break 
        else:   
             print("Đây là tam giác thương")
             break 
    else: 
        print("Vui lòng nhập lại hế số a, b, c")
        a =float(input("Nhập hệ số a: "))
        b =float(input("Nhập hệ số b: "))
        c =float(input("Nhập hệ số c: "))
else: 
    print("Hệ số không đúng điều kiện")
   
