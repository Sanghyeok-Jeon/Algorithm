import sys
sys.stdin = open('BOJ_2460.txt', 'r')

nowPassenger = 0
maxPassenger = 0
for _ in range(10):
    outPassenger, inPassenger = map(int, input().split())
    nowPassenger += inPassenger - outPassenger
    maxPassenger = max(maxPassenger, nowPassenger)
print(maxPassenger)