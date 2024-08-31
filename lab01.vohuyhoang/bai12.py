# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:52:27 2024

@author: VoHuyHoang
"""
import random 
# a. 0 đến 100
print("a. Xuất ra một số (nguyên, thực) ngẫu nhiên từ 0 - 100")
print("Kết quả số nguyên là: ",random.choice(range(0, 100)))
print ("Kết quả số thực là: ", random.uniform(0, 100))
#b. 50 đến 99
print("b. Xuất ra một số (nguyên, thực) ngẫu nhiên từ 55 - 99")
print("Kết quả số nguyên là: ",random.choice(range(50, 99)))
print ("Kết quả số thực là: ", random.uniform(50, 99))
#c. -39 đến 79
print("c. Xuất ra một số (nguyên, thực) ngẫu nhiên từ (-39) - 79") 
print("Kết quả số nguyên là: ",random.choice(range((-39), 79)))
print ("Kết quả số thực là: ", random.uniform((-39), 79))
#d. -79 đến - 39
print("d. Xuất ra một số (nguyên, thực) ngẫu nhiên từ (-79) - (-39)")
print("Kết quả số nguyên là: ",random.choice(range((-79), (-39))))
print ("Kết quả số thực là: ", random.uniform((-79),(-39)))
