import sys
sys.stdin = open('BOJ_20254.txt', 'r')

Ur, Tr, Uo, To = map(int, input().split())
print(Ur*56 + Tr*24 + Uo*14 + To*6)