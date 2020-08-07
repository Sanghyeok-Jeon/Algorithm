import sys
sys.stdin = open('1936.txt', 'r')

a, b = map(int, input().split())
result = a-b

if result == 1 or -2:
    print('A')
else:
    print('B')