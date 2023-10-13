import sys
sys.stdin = open('BOJ_27433.txt', 'r')

def Factorial(n):
    if n == 0:
        return 1

    if n == 1:
        return 1

    return n * Factorial(n-1)

N = int(input())
print(Factorial(N))
