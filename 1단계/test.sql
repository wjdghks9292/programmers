# 상위 N개
SELECT NAME FROM ANIMAL_INS
    ORDER BY DATETIME
    LIMIT 1

# 여러 기준 정렬
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS
    ORDER BY NAME, DATETIME DESC


# WHERE 의 순서와 빈 값 찾기
SELECT ANIMAL_ID FROM ANIMAL_INS
    WHERE NAME IS NOT NULL  
    ORDER BY ANIMAL_ID


# 문자열이 포함되어있는지 확인
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS FROM FOOD_FACTORY
    WHERE ADDRESS LIKE "%강원도%"
    ORDER BY FACTORY_ID	

# 특정 열의 조건식을 다는 방법
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS,
    CASE 
        WHEN FREEZER_YN IS NULL THEN 'N'
        ELSE FREEZER_YN
    END AS FREEZER_YN
        FROM FOOD_WAREHOUSE
    
    WHERE ADDRESS LIKE "%경기도%"
    ORDER BY WAREHOUSE_ID

#원하는 것만 카운트
SELECT COUNT(*) AS USERS FROM USER  _INFO
    WHERE AGE IS NULL;

#날짜 형식 변경
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD FROM DOCTOR
    WHERE MCDP_CD IN ("CS", "GS")
    ORDER BY HIRE_YMD DESC, DR_NAME

#조건문 두개 쓰는법과 범위 정하는 법
SELECT COUNT(*) AS USERS FROM USER_INFO
    WHERE 
        JOINED LIKE '2021%' AND
        AGE >= 20 AND AGE <= 29;