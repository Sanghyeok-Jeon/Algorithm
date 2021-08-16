import sys
sys.stdin = open('BOJ_5565.txt', 'r')

total = int(input())
for _ in range(9):
    total -= int(input())
print(total)