def solution(money):
    cup = money // 5500
    change = money % 5500
    answer = [cup, change]
    return answer