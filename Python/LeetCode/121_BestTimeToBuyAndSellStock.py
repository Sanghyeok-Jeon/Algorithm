# 풀이 2
import sys


def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

# 풀이 1 - 타임아웃
# def maxProfit(self, prices: List[int]) -> int:
#     max_price = 0
#
#     for i, price in enumerate(prices):
#         for j in range(i, len(prices)):
#             max_price = max(price[j] - price, max_price)
#
#     return max_price