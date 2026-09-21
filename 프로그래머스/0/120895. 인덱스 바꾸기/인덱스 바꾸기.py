def solution(my_string, num1, num2):
    
    # string을 list로 변환
    arr = list(my_string)
    
    arr[num1], arr[num2] = arr[num2], arr[num1]
    
    # 문자열 리스트를 하나의 문자열로 합침
    answer = ''.join(arr)
        
    return answer