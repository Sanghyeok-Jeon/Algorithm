import sys
sys.stdin = open('BOJ_2455.txt', 'r')

maxNum, nowNum = 0, 0
for _ in range(4):
    inNum, outNum = map(int, input().split())
    nowNum += outNum - inNum
    maxNum = max(maxNum, nowNum)

print(maxNum)