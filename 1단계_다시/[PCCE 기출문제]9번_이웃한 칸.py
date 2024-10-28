def solution(board, h, w):
    n = len(board)
    answer = 0
    if h > 0:
        if board[h][w] == board[h-1][w]:
            answer += 1
    if h < n-1:
        if board[h][w] == board[h+1][w]:
            answer += 1
    if w > 0:
        if board[h][w] == board[h][w-1]:
            answer += 1
    if w < n-1:
        if board[h][w] == board[h][w+1]:
            answer += 1
    return answer