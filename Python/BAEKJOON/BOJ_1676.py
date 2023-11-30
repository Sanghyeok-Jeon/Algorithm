import sys
sys.stdin = open('BOJ_1676.txt', 'r')

N = int(sys.stdin.readline())

cnt5 = 0
while N:
    N //= 5
    cnt5 += N

print(cnt5)