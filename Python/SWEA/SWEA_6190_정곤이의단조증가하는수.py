import sys
sys.stdin = open('6190.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))

    max_num = 0
    for i in range(N):
        for j in range(N):
            if i < j:
                danzo = 1
                num = str(data[i]*data[j])
                for k in range(len(num)-1):
                    if num[k] > num[k+1]:
                        danzo = 0
                        break
                if danzo and int(num) > max_num:
                    max_num = int(num)

    print('#{} {}'.format(tc+1, max_num if max_num else -1))
