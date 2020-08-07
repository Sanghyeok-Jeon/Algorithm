import sys
sys.stdin = open('1493.txt', 'r')

group = [0]
for n in range(1, 300):
    group.append(n * (n-1)//2 + 1)

def find_xy(num):
    group_num = 0
    num_x = 0
    num_y = 0
    for i in range(1, len(group)):
        if group[i] <= num < group[i + 1]:
            group_num = i
            num_x = 1 + num - group[i]
            num_y = i - (num - group[i])
            break
    return [group_num, num_x, num_y]

T = int(input())

for tc in range(T):
    p, q = map(int, input().split())

    group_p = find_xy(p)
    group_q = find_xy(q)

    black_star = group[group_p[1] + group_q[1] + group_p[2] + group_q[2] - 1] + (group_p[1] + group_q[1] - 1)

    print('#{} {}'.format(tc+1, black_star))