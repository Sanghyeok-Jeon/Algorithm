import sys
sys.stdin = open('BOJ_2845.txt', 'r')

L, P = map(int, input().split())
data = list(map(int, input().split()))

for i in range(5):
    data[i] -= L * P

print(*data)