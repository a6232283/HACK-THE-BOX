#/bin/bash

data=$(cat passwd2); 
for i in {1..13}; 
do 
data=$(echo $data | tr ' ' '\n' |base64 -d); 
done; 
echo $data
