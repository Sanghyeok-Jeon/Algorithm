import sys
sys.stdin = open('BOJ_1269.txt', 'r')

n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B) + len(B-A))