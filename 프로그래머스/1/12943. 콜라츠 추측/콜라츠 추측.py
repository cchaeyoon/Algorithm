def solution(num):
    repeat = 0
    while num != 1 and repeat != 500:
        if num % 2 == 0:
            num = num / 2
        elif num % 2 == 1:
            num = num * 3 + 1
        repeat += 1
        
    if repeat == 500:
        answer = -1
    else:
        answer = repeat
    return answer