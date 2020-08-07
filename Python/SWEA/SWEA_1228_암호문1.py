import sys
sys.stdin = open('1228.txt', 'r')

T = 10

for tc in range(T):
    N = int(input())
    original_code = list(map(int, input().split()))
    M = int(input())
    data = list(input().split())

    cnt_I = 0
    i = 0
    while cnt_I != M:
        new_code = []
        cnt_I += 1
        new_code += original_code[:int(data[i+1])]
        new_code += data[i+3:i+3+int(data[i+2])]
        new_code += original_code[int(data[i+1]):]
        original_code = new_code
        i += 2 + int(data[i+2]) + 1

    print('#{}'.format(tc+1), end=' ')
    for i in range(10):
        print(int(original_code[i]), end=' ')
    print()
