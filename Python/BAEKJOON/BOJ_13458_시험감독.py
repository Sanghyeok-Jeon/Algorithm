import sys
sys.stdin = open('BOJ_13458.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    need = 0

    for i in range(N):
        person = A[i]
        need += 1
        if person > B:
            need += (person-B) // C
            if (person-B) % C:
                need += 1

    print(need)