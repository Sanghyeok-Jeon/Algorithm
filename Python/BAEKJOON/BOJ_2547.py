import sys
sys.stdin = open('BOJ_2547.txt', 'r')

T = int(input())
for _ in range(T):
    input()

    student = 0
    candy = 0
    N = int(input())
    for _ in range(N):
        candy += int(input())
        student += 1

    print('YES' if not candy%student else 'NO')

