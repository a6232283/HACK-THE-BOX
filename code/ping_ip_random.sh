for i in {1..255}; do
	IP="10.10.11.$i";
		ping -c 1 "$IP" &>/dev/null && echo $IP "sussecc";
done
