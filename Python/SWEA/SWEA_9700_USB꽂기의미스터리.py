import sys
sys.stdin = open('9700.txt', 'r')

T = int(input())

for tc in range(T):
    p, q = map(float, input().split())

    # s1 : 1번만 뒤집기
    # 처음 뒤집어서 꽂음 + 다시 뒤집어서 올바른 면으로 꽂기 성공
    s1 = (1-p) * q

    # s2 : 2번 뒤집기
    # 처음 올바른면, 처음에 꽂기 실패 후 뒤집었다가 다시 뒤집어서 꽂기 성공
    s2 = p * (1-q) * q

    print('#{} {}'.format(tc+1, 'YES' if s1 < s2 else 'NO'))