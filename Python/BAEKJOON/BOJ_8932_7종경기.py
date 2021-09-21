import sys
sys.stdin = open('BOJ_8932.txt', 'r')

data = [(9.23076, 26.7, 1.835),
        (1.84523, 75, 1.348),
        (56.0211, 1.5, 1.05),
        (4.99087, 42.5, 1.81),
        (0.188807, 210, 1.41),
        (15.9803, 3.8, 1.04),
        (0.11193, 254, 1.88)]

T = int(input())
for t in range(T):
    score = 0
    pList = list(map(int, input().split()))
    for i in range(7):
        A, B, C = data[i]
        P = pList[i]
        if B <= P:
            score += int(A * (P - B) ** C)
        else:
            score += int(A * (B - P) ** C)

    print(score)