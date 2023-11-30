import sys
sys.stdin = open('BOJ_2720.txt', 'r')

T = int(input())
for _ in range(T):
    change = int(input())
    coin = [0, 0, 0, 0]

    Quarter = change // 25
    coin[0] = Quarter
    change %= 25

    Dime = change // 10
    coin[1] = Dime
    change %= 10

    Nickel = change // 5
    coin[2] = Nickel
    change %= 5

    Penny = change
    coin[3] = Penny

    print(*coin)