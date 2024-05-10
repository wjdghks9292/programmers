def solution(d, budget):
    answer = 0
    
    d.sort(reverse=False)
    print(d)
    for i in d:
        if budget - i >= 0:
            budget -= i
            answer += 1
        else:
            break
    return answer