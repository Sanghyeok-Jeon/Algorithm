import sys
sys.stdin = open('BOJ_2675.txt', 'r')

T = int(input())
for tc in range(T):
    R, S = input().split()

    for i in S:
        for j in range(int(R)):
            print(i, end="")
    print()