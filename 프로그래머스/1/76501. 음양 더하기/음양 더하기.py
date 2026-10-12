def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)): # [0, 3)
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer