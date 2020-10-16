import sys
sys.stdin = open('BOJ_9655.txt', 'r')

print('SK' if int(sys.stdin.readline()) % 2 else 'CY')