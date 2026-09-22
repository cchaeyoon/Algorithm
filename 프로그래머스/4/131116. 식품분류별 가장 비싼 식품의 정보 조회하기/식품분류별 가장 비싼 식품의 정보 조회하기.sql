SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
# AND가 OR보다 우선순위가 높기에 OR로 하나하나 비교하지 않고 IN으로 처리
WHERE CATEGORY IN ('과자', '국', '김치', '식용유') 
    AND 
        # CATEGORY로 묶으므로 SELECT에도 CATEGORY, PRICE 컬럼을 가져와야함
        (CATEGORY, PRICE) IN
        (SELECT CATEGORY, MAX(PRICE) 
         FROM FOOD_PRODUCT 
         WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
         GROUP BY CATEGORY)
ORDER BY PRICE DESC;