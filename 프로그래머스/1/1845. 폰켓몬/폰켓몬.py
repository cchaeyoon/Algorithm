def solution(nums):
    answer = 0
    if len(set(nums)) > (len(nums)/2) : 
        answer = (len(nums) / 2) 
    else:
        # 중복 제거한 set의 길이
        answer = len(set(nums)) 
    return answer