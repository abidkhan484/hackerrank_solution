import collections

def counting_sort(li):
    mylist = []
    for i in range(100):
        if li:
            mylist.extend(li[i])

    del li
    packet = collections.Counter(mylist)

    for i in range(len(mylist)):
        if packet[mylist[i]] == 1:
            print(mylist[i], end=' ')
        else:
            print('-',end=' ')
    
    return mylist


n = int(input().strip())
mylist = [[] for i in range(100)]

for i in range(n):
    m, a = input().split()
    m = int(m)
    mylist[m].append(a)

li = counting_sort(mylist)

'''
input:
20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the

output:
- - - - - to be or not to be - that is the question - - - -
'''
