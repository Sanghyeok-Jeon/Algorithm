import sys
sys.stdin = open('BOJ_2525.txt', 'r')

A, B = map(int, input().split())
C = int(input())

minute = (B + C) % 60
hour = (A + (B + C) // 60) % 24

print(hour, minute)