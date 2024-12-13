import re

# 讀取 1.txt 文件
with open('1.txt', 'r') as f:
    lines = f.readlines()  # 逐行讀取文件內容

# 初始化變數
lis, temp, word = [], '', ''

# 獲取域名
for line in lines:
    # 將 .microsofto365. 替換為 '111'
    st = re.sub(r'\.microsofto365\.*', '111', line)
    
    # 搜尋 'Name: ' 後面的內容直到 '111'
    st = re.search(r'Name: (.*?)111', st)
    if st:
        # 提取域名，刪除開頭的 18 個字元並將 '.' 移除
        lis.append(st.group(1)[18:].replace('.', ''))

# 將結果轉換為字符串
for line in lis:
    # 將每個十六進位字串轉換為對應的 ASCII 字元
    for i in range(0, len(line), 2):
        temp += chr(int(line[i:i+2], 16))  # 將兩個字元一組的十六進位轉為字符
    word += temp  # 將解碼後的字串添加到最終結果
    temp = ''  # 清空暫存變數

# 將解碼後的結果寫入 2.txt
with open('2.txt', 'w') as f:
    f.write(word)
