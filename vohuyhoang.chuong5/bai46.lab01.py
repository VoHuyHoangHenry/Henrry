# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:51:09 2024

@author: VoHuyHoang 
"""
n = 979
# Duyệt qua các giá trị x
for x in range(1, n // 2 + 1):  
    # Duyệt qua các giá trị y
    for y in range(1, n // 7 + 1):  
        # Duyệt qua các giá trị z
        for z in range(1, n // 9 + 1):  
            # Kiểm tra xem 2x + 7y + 9z có bằng 979 không
            if x > 0 and y > 0 and z > 0:
                if 2 * x + 7 * y + 9 * z == n:
                    print(f"x = {x}, y = {y}, z = {z}")
           