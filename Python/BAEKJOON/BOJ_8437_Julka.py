import sys
sys.stdin = open('BOJ_8437.txt', 'r')

total, diff = int(input()), int(input())
print((total+diff)//2)
print((total+diff)//2-diff)