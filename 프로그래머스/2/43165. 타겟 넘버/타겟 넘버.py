def solution(numbers, target):
    answer = 0
    sum = 0
    
    def dfs(index, sum):
        nonlocal answer
        
        # 인덱스가 끝에 도달하면 합과 비교
        if index == len(numbers):
            if sum == target:
                # 값이 target과 같으면 +1
                answer += 1
            return
        
        # +인지 -인지 쪼개지는 부분
        dfs(index + 1, sum +numbers[index])
        dfs(index + 1, sum - numbers[index])
            
    dfs(0, 0)
    
    return answer