import sys
sys.stdin = open('BOJ_5598.txt', 'r')

afterConv = input()

beforeConv = ''
for s in afterConv:
    if ord(s) > ord('C'):
        beforeConv += chr(ord(s) - 3)
    else:
        beforeConv += chr(ord('Z') - ord('C') + ord(s))

print(beforeConv)