import sys

input=sys.stdin.readline

s=input().strip()
t=input().strip()

rr=len(t) - len(s)
for _ in range(rr):
    if t[-1]=='A':
        t=t[:-1]

    elif t[-1]=='B':
        t=t[:-1][::-1]


if s==t:
    print(1)
else:
    print(0)



