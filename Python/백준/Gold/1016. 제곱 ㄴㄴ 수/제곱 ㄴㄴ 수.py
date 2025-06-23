import sys
input=sys.stdin.readline
a,b=map(int,input().split())

i=2
issq=[True]*(b-a+1)

while i * i <= b:
    sq = i * i
    start = ((a+sq-1) // sq) * sq
    for j in range(start, b + 1, sq):
        issq[j - a] = False 
    i += 1

print(sum(issq))