import sys
input=sys.stdin.readline

def eratosthenes(n):
    sieve = [True]*(n+1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i]]

a,b=map(int,input().split())

res=0


for i in eratosthenes(int(b**(1/2))+1):
    power = i * i
    while power <= b:
        if power >= a:
            res += 1
        power *= i


print(res)