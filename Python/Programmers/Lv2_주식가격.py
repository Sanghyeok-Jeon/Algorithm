import collections

def solution(prices):
    answer = []
    qPrices = collections.deque(prices)

    while qPrices:
        price = qPrices.popleft()
        timeSurvive = 0
        for p in qPrices:
            timeSurvive += 1
            if price > p:
                break
        answer.append(timeSurvive)

    return answer