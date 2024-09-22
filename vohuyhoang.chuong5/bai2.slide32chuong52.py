# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 00:43:54 2024

@author: ADMIN
"""

danh_sach = [a for a in range(2020, 3839, 2)]
print("Danh sách số chẵn nguyên từ 2020 đến 3839: ", danh_sach)
chia = [b for b in danh_sach if b % 9 == 0]
print ("Danh sách số chia hết cho 9 từ danh sách thu được: ", chia)
for i in chia:
    print( i, end='\t' )
