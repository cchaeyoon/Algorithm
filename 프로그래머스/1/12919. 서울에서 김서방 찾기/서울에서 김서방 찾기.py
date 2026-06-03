def solution(seoul):
    index = 0
    locate = 0
    for i in seoul:
        if i == "Kim":
            locate = index
            break
        else:
            index += 1
            continue
    answer = f'김서방은 {locate}에 있다'
    return answer