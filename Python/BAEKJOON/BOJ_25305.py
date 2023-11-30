import sys
sys.stdin = open('BOJ_25305.txt', 'r')

N, k = map(int, input().split())
x = sorted(list(map(int, input().split())))

print(x[N-k])