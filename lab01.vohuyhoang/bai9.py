# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:36:26 2024

@author: 
"""
print("============MENU============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("============================")
a = input ("Mời bạn lựa chọn món: ")
print("============================")
if a == "1":
    print("Món bạn chọn là hu tieu")
elif a == "2":
    print("Món bạn chọn là chao long")
elif a == "3":
    print("Món bạn chọn là banh canh")
elif a == "4":
    print("Món bạn chọn là bun rieu")
elif a == "5":
    print("Món bạn chọn là pho bo")
else:
    print("Món bạn chọn không có trong MENU")
