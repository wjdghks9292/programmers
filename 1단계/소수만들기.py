from itertools import combinations

def solution(nums):
    answer = 0
     
    for a in combinations(nums, 3):
        temp = sum(a)
        res = 0
        for b in range(2, int(temp**0.5)+1):
            if temp % b == 0:
                res = -1
                break
        if res == 0:
            answer += 1
    

    return answer