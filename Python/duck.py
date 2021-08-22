## 첫번쨰 생각한 방법은 ~~ 였고 그 방식으로 풀다가 속도가 너무 많이 나올 것 같아서(Big O 첨가)
## 이런 방법으로 풀었다.


# 평소에 막연하게 쓰던 자료형을 이번 문제를 통해서 다시 돌아보게 되었다.
# 아주 큰 수를 많이 다뤄보지 않아서 조금 헤멨다.
# 첫번째로 생각한 방법은 DFS방식이었는데(DFS가 어떻게 하는건지 개념만 찾아보삼)
##################### 1번 문제 ########################
n, k = 31, 31
answer = 1
for i in range(n-k+1, n+1):
    answer *= i
    answer %= 10007

duck = 1
for j in range(1, k+1):
    duck *= j
    duck %= 10007

result = answer**2 // duck

print(result % 10007)



# 
# ##################### 2번 문제 #################
# def MaxSum(arr, l, k):
#     result = 0
#     for i in range(k):
#         result += arr[i]
#
#     nowSum = result
#     for i in range(k, l):
#         nowSum += arr[i] - arr[i-k]
#         result = max(result, nowSum)
#
#     return result
#
# data = [5, 1, 9, 8, 10, 5]
# #data = [10, 1, 10, 1, 1, 4, 3, 10]
# k = 3
# l = len(data)
# answer = MaxSum(data, l, k)
#
# print(answer)


# 처음에는 이진수로 변환한 후에 답을 찾으려함
# 그런 과정이 필요하지 않다는 걸 깨닫고 더 간단한 방법으로 접근해봄
############### 3번 문제 ###############
#
# def CntOne(n):
#     cntOne = 0
#     while n:
#         tmp = n % 2
#         if tmp:
#             cntOne += 1
#         n //= 2
#     return cntOne
#
# n = 9
# target = CntOne(n)
# result = 0
#
# for i in range(1, n):
#     tmp = CntOne(i)
#     if target == tmp:
#         result += 1
#
# print(result)