import sys
sys.stdin = open('BOJ_10039.txt', 'r')

total = 0
for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    total += n

print(total // 5)