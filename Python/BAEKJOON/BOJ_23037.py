import sys
sys.stdin = open('BOJ_23037.txt', 'r')

N = input()
result = 0
for n in N:
    result += int(n) ** 5

print(result)