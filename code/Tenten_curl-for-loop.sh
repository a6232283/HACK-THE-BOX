#/bin/bash

for (( i=1; i<=30; i=i+1 )); do
    echo -n "$i: "
    curl -s http://tenten.htb/index.php/jobs/apply/$i/ | grep '<title>'
done
