import sys
sys.stdin = open('BOJ_17219.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

dictPW = {}
for _ in range(N):
    address, password = sys.stdin.readline().split()
    dictPW[address] = password

for _ in range(M):
    target = sys.stdin.readline().rstrip()
    print(dictPW[target])