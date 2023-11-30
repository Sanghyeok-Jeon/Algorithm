import sys
sys.stdin = open('BOJ_1637.txt', 'r')

def binarySearch(mid):
    temp_sum = 0
    for i in range(N):
        if mid >= A[i]:
            temp_sum += (min(mid, C[i]) - A[i]) // B[i] + 1
    return temp_sum

N = int(input())
A, B, C = [], [], []
for i in range(N):
    a, c, b = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

MAX = 2147483647
left, right = 1, MAX
while left < right:
    mid = (left + right) // 2
    if not binarySearch(mid) % 2:
        left = mid + 1
    else:
        right = mid

if left == MAX:
    print('NOTHING')
else:
    print('{} {}'.format(left, binarySearch(left) - binarySearch(left-1)))

