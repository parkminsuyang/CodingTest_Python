import sys

input = sys.stdin.readline

mid=list(input().strip())

stck=[]
end=[]


for m in mid:
    if 'A'<=m<='Z':
        end.append(m)

    elif m=='(':
        stck.append(m)

    elif m==')':
        while stck and stck[-1]!='(':
            end.append(stck.pop())

        stck.pop()

    elif m in ['*','/']:
        while stck and stck[-1] in ['*','/']:
            end.append(stck.pop())
        stck.append(m)


    elif m in ['+', '-']:
        while stck and stck[-1]!='(':
            end.append(stck.pop())
        stck.append(m)

while stck:
    cur = stck.pop()
    if cur == '(' or cur == ')':
        continue
    else:
        end.append(cur)

print(''.join(end))