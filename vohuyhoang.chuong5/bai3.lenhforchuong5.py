# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 14:15:56 2024

@author: VoHuyHoang 
"""
import random
so_phan_tu = random.randint(20, 30)
print(f"Số lượng phần tử: {so_phan_tu}")
danh_sach = [random.uniform(18, 99)**2 for a in range(so_phan_tu)]
print("Danh sách các giá trị bình phương:", danh_sach)



