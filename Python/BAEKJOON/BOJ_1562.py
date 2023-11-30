def check(nowNum, lenNum, nowDigit):
    if nowDigit < 0 or nowDigit > 9:
        return 0

    if lenNum == N:
        if nowNum == (1 << 10) - 1:
            return 1
        else:
            return 0

    if dp[nowNum][lenNum][nowDigit] != -1:
        return dp[nowNum][lenNum][nowDigit]

    dp[nowNum][lenNum][nowDigit] = 0

    if nowDigit == 0:
        dp[nowNum][lenNum][nowDigit] += check(nowNum | (1 << (nowDigit+1)), lenNum+1, nowDigit+1)
        dp[nowNum][lenNum][nowDigit] %= mod
    elif nowDigit == 9:
        dp[nowNum][lenNum][nowDigit] += check(nowNum | (1 << (nowDigit-1)), lenNum+1, nowDigit-1)
        dp[nowNum][lenNum][nowDigit] %= mod
    else:
        dp[nowNum][lenNum][nowDigit] += check(nowNum | (1 << (nowDigit+1)), lenNum+1, nowDigit+1)
        dp[nowNum][lenNum][nowDigit] %= mod
        dp[nowNum][lenNum][nowDigit] += check(nowNum | (1 << (nowDigit-1)), lenNum+1, nowDigit-1)
        dp[nowNum][lenNum][nowDigit] %= mod

    return dp[nowNum][lenNum][nowDigit]

N = int(input())
mod = 1000000000
dp = [[[-1]*11 for _ in range(101)] for _ in range(1 << 11)]

answer = 0
for i in range(1, 10):
    answer += check(1 << i, 1, i)
    answer %= mod

print(answer)