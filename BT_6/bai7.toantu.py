# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:12:57 2024

@author: vohuyhoang
"""
print("============* MENU *============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("================================")
k = input("Moi ban chon mon an: ",)
print("================================")
if k == '1':
    print("Mon ban chon la Hu tieu.")
elif k == '2':
    print("Mon ban chon la Chao long.")
elif k == '3':
    print("Mon ban chon la Banh canh.")
elif k == '4':
    print("Mon ban chon la Bun rieu.")
elif k == '5':
    print("Mon ban chon la Pho bo.")
else:
    print("Vui long chon mon trong Menu!")
