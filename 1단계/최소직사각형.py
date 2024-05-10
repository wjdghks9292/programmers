def solution(sizes):
    width = []
    length = []
    
    for size in sizes:  
        size.sort()
        width.append(size[0])
        length.append(size[1])
            
    return max(width) * max(length)