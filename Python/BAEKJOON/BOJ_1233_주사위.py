import sys
sys.stdin = open('BOJ_1233.txt', 'r')

S1, S2, S3 = map(int, input().split())
nums = [0] * 81
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            nums[i+j+k] += 1
print(nums.index(max(nums)))