# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:16:04 2024

@author: VoHuyHoang
"""
tong_chan = 0
tong_le = 0
for i in range(101):
  if i % 2 == 0:
    tong_chan += i
  else:
    tong_le += i

print("Tổng các số chẵn từ 0 đến 100 là:", tong_chan)
print("Tổng các số lẻ từ 0 đến 100 là:", tong_le)