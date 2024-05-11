def solution(data, ext, val_ext, sort_by):
    filtered_date =[]
    dic = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    
    for d in data:
        if d[dic[ext]] < val_ext:
            filtered_date.append(d)
            
    filtered_date = sorted(filtered_date, key=lambda x : x[dic[sort_by]])
    
    return filtered_date