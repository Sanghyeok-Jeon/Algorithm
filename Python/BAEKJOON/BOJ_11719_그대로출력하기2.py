import sys
sys.stdin = open('BOJ_11719.txt', 'r')

while True:
    try:
        print(input())
    except EOFError:
        break