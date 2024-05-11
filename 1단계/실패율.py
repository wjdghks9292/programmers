def solution(N, stages):
    user = len(stages)
    answer = []
    order = []
    for i in range(1, N+1):
        if i in stages:
            answer.append(stages.count(i) / len(stages))
            remove_set = {i}
            stages = [j for j in stages if j not in remove_set]
        else:
            answer.append(0)
    
    for i in range(len(answer)):
        max_arr = max(answer)
        order.append(answer.index(max_arr)+1)
        answer[answer.index(max_arr)] = -1

    return order