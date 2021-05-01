import sys
sys.stdin = open('BOJ_11024.txt', 'r')

N = int(input())
for _ in range(N):
    print(sum(map(int, input().split())))