from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os

def decrypt(key, filename):
    chunksize = 64*1024  # 定義每次讀取的塊大小
    outputFile = "de_" + filename  # 解密後的檔案名
    
    with open(filename, 'rb') as infile:
        # 讀取檔案大小和 IV
        filesize = int(infile.read(16).decode('utf-8'))
        IV = infile.read(16)
        
        # 初始化解密器
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        
        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                
                if len(chunk) == 0:
                    break
                
                decrypted_chunk = decryptor.decrypt(chunk)
                
                # 如果解密塊超過原始檔案大小，僅寫入到檔案大小的部分
                if len(decrypted_chunk) >= filesize:
                    decrypted_chunk = decrypted_chunk[:filesize]
                    outfile.write(decrypted_chunk)
                    break
                
                outfile.write(decrypted_chunk)

def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

# 使用示例
password = "sahay"
key = getKey(password)
decrypt(key, "enim_msg.txt")  # 解密檔案名
