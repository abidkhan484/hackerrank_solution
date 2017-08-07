#! /bin/python3

import sys
import re

n = int(input().strip())

for i in range(n):
    temp = input().strip()
    pattern = r"[0-9][+.-]"
    l = 0
    for j in temp:
        if (bool(re.search(pattern, j))) is False:
            print(j)
            break
    else:
        l = 1

    if (l==0):
        print('True')
    else:
        print('False')
