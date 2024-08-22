from Crypto.Hash import SHA256
from Crypto.Cipher import AES

def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = "en" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV =Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))


def getKey(password):
            hasher = SHA256.new(password.encode('utf-8'))
            return hasher.digest()

#撰寫以下為解碼code。
def decrypt(key, filename):
    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16).decode('utf-8'))  # 讀取檔案大小
        IV = infile.read(16)  # 讀取初始化向量
        encrypted = infile.read()  # 讀取加密內容

    decryptor = AES.new(key, AES.MODE_CBC, IV)  # 創建 AES CBC 模式的解密器
    decrypted = decryptor.decrypt(encrypted)  # 解密內容

    # 去除填充
    decrypted = decrypted.rstrip(b' ')  # 去除填充的空格

    # 寫入解密後的檔案
    outputFile = "de_" + filename  # 解密後的檔案名稱
    with open(outputFile, 'wb') as outfile:
        outfile.write(decrypted)  # 寫入解密後的內容

# 使用範例：解密檔案
decrypt(getKey("sahay"), "enim_msg.txt")
