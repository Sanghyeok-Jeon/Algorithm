import sys
sys.stdin = open('BOJ_10951.txt', 'r')

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break