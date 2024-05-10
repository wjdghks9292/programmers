def solution(n, m):

    if n > m:
        n, m = m, n
        
    l = n * m
    
    big_n = n
    big_m = m
    
    while (big_n != big_m):
        if big_n < big_m:
            big_n += n
        else:
            big_m += m
    
    
    return [l//big_n, big_n]