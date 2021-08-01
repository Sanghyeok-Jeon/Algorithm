import sys
sys.stdin = open('BOJ_1598.txt', 'r')

N, M = map(int, input().split())
print(abs((N-1)//4 - (M-1)//4) + abs((N-1)%4 - (M-1)%4))
