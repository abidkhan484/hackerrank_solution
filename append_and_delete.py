#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())


length_s = len(s)
length_t = len(t)

# this will check minimum length for the loop
if length_s>length_t:
    mini = length_t
else:
    mini = length_s

# check how many match on the two string
for i in range(mini):
    if s[i]!=t[i]:
        i -= 1
        break

i += 1

# to check how many mismatch finding here
if i==mini:
    i = k + 1
else:
    length_s -= i
    length_t -= i
    i = length_s + length_t


# logical statement to find the ans
if k < i:
    print('No')
else:
    print('Yes')
