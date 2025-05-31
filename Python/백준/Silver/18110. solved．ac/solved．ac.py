import sys

input=sys.stdin.readline
n=int(input())
if n==0:
    print(0)
    exit()
hard=[int(input()) for _ in range(n)]
cut=int(n * 0.15 + 0.5)
realHard=sorted(hard)[cut:n-cut]

print(int((sum(realHard)/len(realHard))+0.5))