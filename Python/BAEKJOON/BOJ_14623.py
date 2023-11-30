import sys
sys.stdin = open('BOJ_14623.txt', 'r')

B1 = int('0b'+input(),2)
B2 = int('0b'+input(),2)

print(format(B1*B2, 'b'))