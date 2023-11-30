import sys
sys.stdin = open('BOJ_17256.txt', 'r')

ax, ay, az = map(int, input().split())
cx, cy, cz = map(int, input().split())

bx, by, bz = cx - az, cy // ay, cz - ax
print(bx, by, bz)