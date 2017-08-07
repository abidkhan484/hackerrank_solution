#!/bin/python3

import sys


g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    a.reverse(); b.reverse()

    count = 0
    if (a[-1] > x) and (b[-1] > x):
        print(0)
        continue
    
    while (0 < x) and bool(a and b):
        if a[-1] < b[-1]:
            tmp = a.pop()
            if tmp <= x:
                print(tmp)
                count += 1
        elif a[-1] >= b[-1]:
            tmp = b.pop()
            if tmp <= x:
                print(tmp)
                count += 1
        x -= tmp

    if x > 0:
        temp = a or b
        while x > 0:
            tmp = temp.pop()
            if tmp <= x:
                count += 1
            x -= tmp
    #print(count)
