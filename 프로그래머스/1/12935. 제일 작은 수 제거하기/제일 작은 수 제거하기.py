def solution(arr):
    answer = []
    min_value = min(arr)
    arr.remove(min_value)
    if arr == []:
        answer.append(-1)
    else:
        answer = arr
    return answer