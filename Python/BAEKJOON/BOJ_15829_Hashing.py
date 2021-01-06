import sys
sys.stdin = open('BOJ_15829.txt', 'r')

L = int(input())
hashStr = input()
M = 1234567891

result = 0
for i in range(L):
    result += (ord(hashStr[i])-ord('a')+1) * (31**i)

print(result % M)