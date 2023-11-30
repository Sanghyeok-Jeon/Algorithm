import sys
sys.stdin = open('BOJ_10817.txt', 'r')

data = list(map(int, input().split()))
data.sort()
print(data[1])