#/bin/bash

for x in 40809 50212 46969;
	do 
		nmap -sU -Pn --max-retries 0 -p $x 10.10.10.96;
		#--max-retries 0: 設定Nmap在沒有收到回應時不進行重試
	done
ssh dorthi@10.10.10.96 -i id_rsa
