# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:39:25 2024

@author: VoHuyHoang
"""
max_sum = 0
a = (0, 0, 0)

# Sử dụng vòng lặp for để duyệt qua các giá trị của x, y, z
for x in range(1, (979//2) + 1):
    for y in range(1, (979- 2*x)//7):
        z = (979 - 2*x - 7*y) // 9
        if 2*x + 7*y + 9*z == 979 and z > 0:
            tong = x + y + z
            if tong > max_sum:
                max_sum = tong
                best_solution = (x, y, z)

print(f"Bộ nghiệm có tổng x + y + z lớn nhất là: x = {best_solution[0]}, y = {best_solution[1]}, z = {best_solution[2]}")