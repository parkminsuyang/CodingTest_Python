#왼괄 오괄 소괄 대괄 맞추기
#괄 사이 문자열도 균형필요
#온점 입력시 종료
import sys

input=sys.stdin.readline




def cnt(mun):
    stack=[]

    for i in mun:
        if i == '(' or i=='[':
            stack.append(i)

        elif i == ')':
            if len(stack)>0 and stack[-1]=='(':
                stack.pop()
            else:
                return 'no'


        elif i == ']':

            if len(stack)>0 and stack[-1] == '[':

                stack.pop()

            else:

                return 'no'
    if len(stack)==0:
        return 'yes'
    else:
        return 'no'

while True:
    mun=input().rstrip()
    if mun == '.':
        break
    print(cnt(mun))