def solution(n, arr1, arr2):
    answer = []
    list = []

    # arr1, arr2을 10진수 -> 2진수
    for i in range(n):
        list.append(bin(arr1[i] | arr2[i])[2:].rjust(n, '0'))
        
    for i in range(n):
        result = ''
        for j in list[i]: # 11111에서 1
            if j == '1':
                result += '#'
            else:
                result += ' '
        answer.append(result)
    return answer