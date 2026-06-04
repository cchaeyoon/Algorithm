def solution(array, commands):
    answer = []
    temp = []
    for i in commands: # [2, 5, 3]
        # 2부터 5까지 슬라이싱
        temp = array[(i[0]-1):i[1]]
        temp.sort()
        answer.append(temp[i[2]-1])
    return answer