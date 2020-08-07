T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    code = []
    decode_num = []

    start_i, start_j = 0, 0
    for i in range(N):
        for j in range(M):
            if j + 6 > M:
                break
            if data[i][j:j+7] in num and data[i][j+7:j+14] in num:
                start_i = i
                start_j = j
                break
        if start_j:
            break

    for k in range(start_j, start_j + 56, 7):
        code.append(data[start_i][k:k+7])

    for m in range(len(code)):
        for n in range(10):
            if code[m] == num[n]:
                decode_num.append(n)

    result = (decode_num[0] + decode_num[2] + decode_num[4] + decode_num[6]) * 3 + (decode_num[1] + decode_num[3] + decode_num[5]) + decode_num[7]

    print('#{} {}'.format(tc+1, sum(decode_num) if result % 10 == 0 else 0))