n = int(input().strip())
li = list(map(int, input().split()))
for i in range(n):
    if li[i] < 0:
        print('False')
        break
else:
    for j in range(n):
        
