import sys
sys.stdin = open('BOJ_1252.txt', 'r')

bin1, bin2 = input().split()
print(bin(int(bin1, 2) + int(bin2, 2))[2:])