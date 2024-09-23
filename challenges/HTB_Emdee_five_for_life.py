from bs4 import BeautifulSoup
import requests
import hashlib

URL = "http://94.237.59.63:54549/"
request = requests.session()
page = request.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

# 尋找所有 h3 標籤
for i in soup.findAll('h3'):
        md5 = (i.get_text())  # 獲取 h3 標籤的文字
        ##print(md5)

hash_object = hashlib.md5(md5.encode())  # 計算 MD5 哈希值
md5_hash = hash_object.hexdigest()
##print(md5_hash)

data = {'hash': md5_hash}  # 準備要發送的數據
output = request.post(url = URL, data = data)  # 發送 POST 請求

print(output.text)  # 輸出回應內容
