def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        quotient, remainder = (n-1) // 3, (n-1) % 3
        return solution(quotient) + '124'[remainder]