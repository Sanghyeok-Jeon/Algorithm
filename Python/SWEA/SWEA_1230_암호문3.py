import sys
sys.stdin = open('1230.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    original_code = list(map(int, input().split()))
    M = int(input())
    data = list(input().split())

    cnt_I = 0
    cnt_D = 0
    cnt_A = 0
    i = 0
    while True:
        if cnt_I + cnt_D + cnt_A == M:
            break
        if data[i] == 'I':
            new_code = []
            cnt_I += 1
            new_code += original_code[:int(data[i + 1])]
            new_code += data[i + 3:i + 3 + int(data[i + 2])]
            new_code += original_code[int(data[i + 1]):]
            original_code = new_code
            i += 2 + int(data[i + 2]) + 1
        elif data[i] == 'D':
            new_code = []
            cnt_D += 1
            new_code += original_code[:int(data[i+1])]
            new_code += original_code[int(data[i+1])+int(data[i+2]):]
            original_code = new_code
            i += 3
        elif data[i] == 'A':
            cnt_A += 1
            original_code += data[i+2: i+2+int(data[i+1])]
            i += 1 + int(data[i+1]) + 1

    print('#{}'.format(tc + 1), end=' ')
    for i in range(10):
        print(int(original_code[i]), end=' ')
    print()