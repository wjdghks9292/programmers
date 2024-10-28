def solution(bandage, health, attacks):
    max_health = health
    count = 0
    
    for attack in attacks:
        time, damage = attack
        
        # 그전 공격과의 시간 차이
        temp = time
        time -= count
        count = temp
        
        # 초당 채력 회복
        health += (time-1)*bandage[1]
        
        # 연속 성공 추가 회복
        if (time-1) // bandage[0] >= 0:
            health += ((time-1) // bandage[0]) * bandage[2]

        # 최대 채력 보정
        if health > max_health:
            health = max_health
        
        # 데미지 계산
        health -= damage
        if health < 1:
            return -1
        
    if health > 0:
        return health
    else:
        return -1