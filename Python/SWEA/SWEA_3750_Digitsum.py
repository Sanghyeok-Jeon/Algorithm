import sys
sys.stdin = open('3750.txt', 'r')

T = int(input())
result = []

for tc in range(T):
    n = int(input())
    ans = n

    while n >= 10:
        temp_sum = 0
        while n >= 10:
            temp_sum += n % 10
            n //= 10
        temp_sum += n
        if temp_sum < 10:
            ans = temp_sum
            break
        else:
            n = temp_sum
    result.append(ans)

x = 1
for i in range(T):
    print('#{} {}'.format(x, result[i]))
    x += 1