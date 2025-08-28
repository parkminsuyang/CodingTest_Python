import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    words=list(input().strip().split())
    for w in words:
        for ch in reversed(w):
            print(ch, end='')
        print(end=' ')
