def solution(price, money, count):
    answer = -1
    temp = 0

    for i in range(1, count + 1): # 4면 1, 2, 3, 4
        temp += price * i
    answer = temp - money
    if temp - money < 0:
        answer = 0
    return answer