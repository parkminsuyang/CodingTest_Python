import sys

input=sys.stdin.readline

t=int(input())
for _ in range(t):
    num,n=map(int,input().split())

    rev_base = ''
    while num>0:
        num, mod = divmod(num, n)
        if mod>=10:
           if mod==10:
               mod='A'
           elif mod==11:
               mod='B'
           elif mod==12:
               mod='C'
           elif mod == 13:
               mod = 'D'
           elif mod == 14:
               mod = 'E'
           elif mod == 15:
               mod = 'D'

        rev_base += str(mod)
    if rev_base==rev_base[::-1]:
        print(1)
    else:
        print(0)