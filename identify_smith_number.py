from math import sqrt
from math import floor

# the function returns all the prime numbers in a number
def all_prime_between_a_num(num):
    mylist = [1]*num
    mylist[0] = 0

    for i in range(1, num, 2):
        mylist[i] = 0

    for i in range(3, floor(sqrt(num))+2, 2):
        if mylist[i-1] == 0:
            continue
        p = i-1+i
        for j in range(p, num, i):
            mylist[j] = 0

    li = [2]
    for i in range(num):
        if mylist[i]:
            li.append(i+1)

    return li

li = all_prime_between_a_num(100000)


#the function return all prime factor in a num
def prime_factorization(n):

    prime_factor = []
    ia = sqrt(n); j = 0
    # here li is the var that 
    while n and (len(li) > j):
        if not n%li[j]:
            n = n // li[j]
            prime_factor.append(li[j])
        else:
            j += 1

    return prime_factor

# this function return the sum of all digits
def digit_sum(n, j=0):
    if not n:
        return j
    return digit_sum(n//10, j+(n%10))


prim = prime_factorization(4937775)
#num = 4937775 #int(input().strip())
#print(1) if sum(prime_factorization(num))==digit_sum(num) else print(0)
