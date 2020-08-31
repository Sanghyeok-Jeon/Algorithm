def solution(numbers, target):
    answer = 0
    N = len(numbers)

    def DFS(idx, N, tmpSum, target, numbers):
        nonlocal answer
        if idx == N:
            if tmpSum == target:
                answer += 1
            return

        DFS(idx + 1, N, tmpSum + numbers[idx], target, numbers)
        DFS(idx + 1, N, tmpSum - numbers[idx], target, numbers)

    DFS(0, N, 0, target, numbers)

    return answer