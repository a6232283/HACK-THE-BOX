#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print(f"{sys.argv[0]} [infile] [outfile]")
    sys.exit(0)

try:
    with open(sys.argv[1], 'r') as f:
        with open(sys.argv[2], 'w') as fout:
            fout.write(f.read().replace('.', 'Ook. ').replace('?','Ook? ').replace('!','Ook! '))
except:
    print("Failed")
