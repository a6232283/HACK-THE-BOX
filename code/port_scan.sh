for port in {1..65535}; 
	do echo > /dev/tcp/172.19.0.1/$port && echo "$port open"; done 2>/dev/null
