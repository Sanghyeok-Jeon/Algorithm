import sys
sys.stdin = open('BOJ_10872.txt', 'r')

N = int(input())

ans = 1
for i in range(1, N+1):
    ans *= i

print(ans)