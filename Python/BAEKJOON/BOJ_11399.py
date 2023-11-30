import sys
sys.stdin = open('BOJ_11399.txt', 'r')

N = int(sys.stdin.readline())
listOrder = list(map(int, sys.stdin.readline().split()))

listOrder.sort()

total = 0
temp = 0
for i in range(N):
    temp += listOrder[i]
    total += temp

print(total)