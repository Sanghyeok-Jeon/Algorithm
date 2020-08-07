import sys
sys.stdin = open('2025.txt', 'r')

N = int(input())

total = 0

for n in range(1, N+1):
    total += n

print(total)