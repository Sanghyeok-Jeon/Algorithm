import sys
sys.stdin = open('BOJ_1026.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

for _ in range(N):
    S += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))

print(S)
