def move_snail(x, y, sec):
    # 방향 전환 순서(상 우 하 좌)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    mode = 0
    length = 1
    changeDirection = 0
    while True:
        # 현재 길이만큼 이동
        for _ in range(length):
            # 입력된 시간만큼 지났을 때 결과값 리턴
            if sec == n:
                return x, y

            x += dx[mode]
            y += dy[mode]

            sec += 1

        # 방향 전환
        mode = (mode + 1) % 4

        # 방향 전환 카운트
        changeDirection += 1

        # 방향 전환 2번이면 길이 + 1
        if changeDirection == 2:
            length += 1
            changeDirection = 0    # 방향 전환 카운트 초기화

n = int(input())
print(*move_snail(0, 0, 0))