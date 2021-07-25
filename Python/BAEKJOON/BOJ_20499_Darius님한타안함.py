import sys
sys.stdin = open('BOJ_20499.txt', 'r')

K, D, A = map(int, input().split('/'))
print('gosu' if K + A >= D and D else 'hasu')