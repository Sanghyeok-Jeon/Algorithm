import sys
sys.stdin = open('BOJ_3053.txt', 'r')

import math
pai = math.pi

R = int(input())

print('{0:6f}'.format(R * R * pai))
print('{0:6f}'.format(R * R * 2))
