import sys
sys.stdin = open('SWEA_4751.txt', 'r')

T = int(input())

for tc in range(T):
    data = input()
    result = ['.', '.', '#', '.', '.']

    for c in data:
        result[0] += '.#..'
        result[1] += '#.#.'
        result[2] += '.' + c + '.#'
        result[3] += '#.#.'
        result[4] += '.#..'

    for i in range(5):
        print(result[i])