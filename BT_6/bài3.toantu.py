# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:07:10 2024

@author: vohuyhoang
"""
n = int(input("Nhập số nguyên dương có 2 chữ số: "))
if 10 <= n <= 99:
    a = n%10
    b = n//10
    c = a + b
    print("Tổng các chữ số là: ", c)
else:
    print("Số không phải là số nguyên dương có 2 chữ số")
    