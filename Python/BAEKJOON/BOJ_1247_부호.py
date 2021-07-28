import sys
sys.stdin = open('BOJ_1247.txt', 'r')

# 리스트 합이 더 빠르다! 그냥 input으로 하면 시간초과!
for _ in range(3):
    S = sum(map(int, (sys.stdin.readline() for _ in range(int(sys.stdin.readline())))))

    if not S:
        print(0)
    else:
        print('+' if S > 0 else '-')

## 시간초과
# for _ in range(3):
#     T = int(input())
#     S = 0
#     for _ in range(T):
#         S += int(input())
#
#     if S > 0:
#         print('+')
#     elif S < 0:
#         print('-')
#     else:
#         print(0)