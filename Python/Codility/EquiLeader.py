def solution(A):
    dictLeft = {}
    dictRight = {}
    for a in A:
        if a in dictRight:
            dictRight[a] += 1
        else:
            dictRight[a] = 1

    leaderLeft = 0
    cntLeaderLeft = 0
    lenRight = len(A)
    lenLeft = 0
    answer = 0
    for a in A:
        dictRight[a] -= 1
        lenRight -= 1

        if a in dictLeft:
            dictLeft[a] += 1
        else:
            dictLeft[a] = 1

        lenLeft += 1

        if dictLeft[a] > cntLeaderLeft:
            leaderLeft = a
            cntLeaderLeft = dictLeft[a]

        if cntLeaderLeft > lenLeft // 2 and dictRight[leaderLeft] > lenRight // 2:
            answer += 1

    return answer