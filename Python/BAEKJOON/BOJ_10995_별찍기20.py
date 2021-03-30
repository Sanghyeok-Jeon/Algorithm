import sys
sys.stdin = open('BOJ_10995.txt', 'r')

N = int(input())
for i in range(N):
    tmpStar = ''
    if i % 2:
        tmpStar += ' '
    tmpStar += '* '* N
    print(tmpStar)