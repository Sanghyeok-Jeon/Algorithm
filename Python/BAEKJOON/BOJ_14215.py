import sys
sys.stdin = open('BOJ_14215.txt', 'r')

abc = sorted(list(map(int, input().split())))
if abc[2] >= sum(abc[:2]):
    print(sum(abc[:2]) * 2 - 1)
else:
    print(sum(abc))