def solution(board, moves):
    answer = 0
    bag = []

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1]:
                if len(bag) > 0 and bag[-1] == board[j][moves[i] - 1]:
                    bag.pop()
                    answer += 2
                else:
                    bag.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break

    return answer