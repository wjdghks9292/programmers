def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        a = format(a, 'b')
        b = format(b, 'b')
        
        a = str(a).zfill(n)
        b = str(b).zfill(n)
        
        line = ''
        for i, j in zip(a,b):
            if (int(i) + int(j)) == 0:
                line += ' '	
            else:
                line += '#'
        answer.append(line)
            
    return answer