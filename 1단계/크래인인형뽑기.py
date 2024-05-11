def solution(board, moves):
    answer = 0
    result = []
    new_board = []
    remove_set = {0}
    board = list(map(list, zip(*board)))
    
    # 0 제거
    for line in board:
        line = [ i for i in line if i not in remove_set]
        new_board.append(line)
    
    for move in moves:
        # 라인에 인형이 있을 때
        if new_board[move-1]:
            temp = new_board[move-1][0]
            new_board[move-1] = new_board[move-1][1:]
            result.append(temp)
            
            # 두 개의 인형이 같으면 제거
            if len(result) > 1:
                if result[-1] == result[-2]:
                    result = result[:-2]
                    answer += 2
            
        # 라인에 인형이 없을 때
        else:
            pass
        
    return answer