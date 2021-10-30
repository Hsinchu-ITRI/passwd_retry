# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:19:28 2021

@author: Win10
"""

password = 'a123456'
guess_total = 0
while True:
    if guess_total < 3:
        guess_passwd = input('請輸入密碼 : ')
        guess_total += 1
        if guess_passwd == password:
            print('登入成功')
            break
        elif guess_total != 3:
             print('密碼錯誤!  還有', 3 - guess_total,'次機會')
           
    else:
        break 
        
         
                
            

  