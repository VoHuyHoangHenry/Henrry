# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:07:10 2024

@author: VoHuyHoang
"""
can_nang = float(input("Nhập số cân nặng (kg): "))
chieu_cao = float(input("Nhập số chiều cao (m): "))
#Công thúc BMI
bmi = (can_nang) / (chieu_cao)**2
if  bmi > 0 and bmi < 18.5:
    print ("Chỉ số MBI của bạn là: ", bmi)
    print("Kết quả kiểm tra sức khỏe MBI: gầy")
elif bmi > 0 and 18.5 <= bmi <= 24.9:
    print ("Chỉ số MBI của bạn là: ", bmi)
    print("Kết quả kiểm tra sức khỏe MBI: bình thường")
elif bmi > 0 and 25 <= bmi <= 29.9:
    print ("Chỉ số MBI của bạn là: ", bmi)
    print("Kết quả kiểm tra sức khỏe MBI: thừa cân")
elif bmi > 0 and 30 <= bmi <= 34.9:
    print ("Chỉ số MBI của bạn là: ", bmi)
    print("Kết quả kiểm tra sức khỏe MBI: béo phì 1")
else:
    print ("Chỉ số MBI của bạn là: ", bmi)
    print("Kết quả kiểm tra sức khỏe MBI: béo phì 2")


