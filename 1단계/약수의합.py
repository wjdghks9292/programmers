def solution(n):
    answer = 0
    ans_list = []
    
    count = int(n**(1/2))
    
    for i in range(1, count+1):
        if n % i == 0:
            ans_list.append(i)
            ans_list.append(n//i)

    answer = sum(ans_list)
    
    if count == n**(1/2):
        answer -= count

    return answer

n = int(input())
print(solution(n))