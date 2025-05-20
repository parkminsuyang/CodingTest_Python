import sys

input=sys.stdin.readline
name=input()

if ('social' in name) or ('history' in name) or('language' in name) or ('literacy' in name):
    print('digital humanities')
else:
    print('public bigdata')