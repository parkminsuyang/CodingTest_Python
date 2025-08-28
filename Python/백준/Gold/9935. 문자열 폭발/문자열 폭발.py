import sys
sys.setrecursionlimit(10**6)

strings=input().strip()
bomb=input().strip()
stack=[]
b=len(bomb)

for s in strings:
    stack.append(s)
    if len(stack)>=b:
        if ''.join(stack[-b:])==bomb:
            for _ in range(b):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")