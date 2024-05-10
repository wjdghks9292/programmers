def solution(s):
    answer = ''
    s_list = s.split(' ')
    
    new_list = []
    for i in s_list:
        new_list.append(i.strip())
    
    ans_list = []
        
    for word in new_list:
        ans_word = ''
        for i, n in enumerate(word):
            if i % 2 == 0:
                ans_word += n.upper()
            else:
                ans_word += n.lower()
            
        ans_list.append(ans_word)
        
    return ' '.join(ans_list)