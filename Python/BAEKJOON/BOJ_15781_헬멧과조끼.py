import sys
sys.stdin = open('BOJ_15781.txt', 'r')

N, M = map(int, input().split())
maxHelmet = max(map(int, input().split()))
maxShield = max(map(int, input().split()))
print(maxHelmet + maxShield)