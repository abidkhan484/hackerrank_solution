from itertools import permutations

a, d = input().split()
d = int(d)

l = list(permutations(a, d))
le = len(l)
l.sort()

print(type(l))

for i in range(le):
    for j in range(d):
        print(l[i][j], end='')
    print()
        
