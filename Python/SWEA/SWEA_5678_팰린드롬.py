import sys
sys.stdin = open('SWEA_5678.txt', 'r')

T = int(input())

for tc in range(T):
    data = input()

    result = 0
    wordLength = len(data)
    while wordLength > 0:
        for i in range(0, len(data)-wordLength):
            if data[i:i+wordLength] == data[i:i+wordLength][::-1]:
                result = wordLength
                break

        if result:
            break

        wordLength -= 1

    print('#{} {}'.format(tc+1, result))