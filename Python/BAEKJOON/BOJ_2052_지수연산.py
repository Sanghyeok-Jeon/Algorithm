import sys
sys.stdin = open('BOJ_2052.txt', 'r')

N = int(input())
num = str(5**N)
print('0.' + '0'*(N-len(num)) + num)