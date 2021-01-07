import sys
import math
sys.stdin = open('BOJ_2609.txt', 'r')

n, m = map(int, sys.stdin.readline().split())
print(math.gcd(n, m))
print(n*m//math.gcd(n, m))