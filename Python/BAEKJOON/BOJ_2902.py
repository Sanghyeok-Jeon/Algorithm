import sys
sys.stdin = open('BOJ_2902.txt', 'r')

result = ''
for name in input().split('-'):
    result += name[0]
print(result)