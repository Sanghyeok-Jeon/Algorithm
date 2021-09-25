import sys
sys.stdin = open('BOJ_16673.txt', 'r')

C, K, P = map(int, input().split())
totalWine = K * (C*(C+1)//2) + P * (C*(C+1)*(2*C+1)//6)
print(totalWine)