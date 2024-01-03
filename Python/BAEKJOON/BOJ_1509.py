# 팰린드롬인지 확인하는 함수
def is_palindrome(s):
    return s == s[::-1]

# 분할 개수 구하는 함수
def palindrome_partition(s):
    n = len(s)
    dp = [int(1e9)] * n    # dp[i]는 문자열 s의 0부터 i까지의 최소 분할 수
    dp[0] = 1

    for end in range(1, n):
        for start in range(end+1):
            if is_palindrome(s[start:end + 1]):
                if start == 0:
                    dp[end] = 1  # start가 0인 경우는 분할이 필요하지 않음
                else:
                    dp[end] = min(dp[end], dp[start - 1] + 1)  # start부터 end까지의 최소 분할 수 갱신

    return dp[n-1] # 문자열 전체의 최소 분할 수 반환

# 입력 받기
s = input()

# 결과 출력
print(palindrome_partition(s))