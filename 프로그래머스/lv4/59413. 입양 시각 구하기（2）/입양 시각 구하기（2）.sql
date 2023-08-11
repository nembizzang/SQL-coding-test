# set 함수 이용
SET @HOUR := -1; # 초기 변수 설정
SELECT (@HOUR := @HOUR+1) HOUR, # HOUR 변수에 +1 반복
        (SELECT COUNT(*)
            FROM animal_outs
            WHERE HOUR(datetime) = @HOUR) COUNT
    FROM animal_outs
    WHERE @HOUR < 23 # 마지막으로 +1한 HOUR가 23이면 반복 멈춤
    ORDER BY HOUR;