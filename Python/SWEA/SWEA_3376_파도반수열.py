import sys
sys.stdin = open('3376.txt', 'r')

T = int(input())
wave = [0, 1, 1]
for i in range(3, 101):
    wave.append(wave[i-3] + wave[i-2])


for tc in range(T):
    N = int(input())

    print('#{} {}'.format(tc+1, wave[N]))