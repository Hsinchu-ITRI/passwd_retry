# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 04:41:19 2021

@author: Win10
"""
password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
    pwd = input('請輸入密碼: ')
    i -= 1
    if pwd == password:
        print('登入成功')
        break
    elif i > 0:
        print('密碼錯誤! 還有', i, '次機會')
    else:
        print('密碼錯誤!沒有機會')
    