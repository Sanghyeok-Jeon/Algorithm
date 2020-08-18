def solution(answers):
    N = len(answers)
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []

    ans_supo1 = 0
    ans_supo2 = 0
    ans_supo3 = 0
    for i in range(N):
        supo1_now = i % 5
        supo2_now = i % 8
        supo3_now = i % 10
        if answers[i] == supo1[supo1_now]:
            ans_supo1 += 1
        if answers[i] == supo2[supo2_now]:
            ans_supo2 += 1
        if answers[i] == supo3[supo3_now]:
            ans_supo3 += 1

    result = [ans_supo1, ans_supo2, ans_supo3]
    visit = [0, 0, 0]
    correct = N
    while True:
        if correct == 0:
            break
        if sum(visit) == 3:
            break
        for i in range(1, 4):
            if result[i - 1] == correct:
                answer.append(i)
                visit[i - 1] = 1
        if answer != []:
            break
        correct -= 1

    return answer