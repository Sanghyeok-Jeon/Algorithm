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