import math

def solution(progresses, speeds):
    days = [] # days = [7, 3, 9] days = [5, 10, 1, 1, 20, 1]
    answer = []
    # [7, 70, 45] -> [7/1 = 7, 반올림(70/30) = 3, 45/5 = 9]
    # 리스트의 끝에서부터 차례로 스택에 넣고, top이 top-1보다 크면 top-1도 꺼냄 -> 반복
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    days.reverse()  # [9, 3, 7]  [1, 20, 1, 1, 10, 5]
    
    while len(days) != 0:
        last = days.pop() # 7, 리스트는 [9, 3]
        func = 1
        while days!= [] and last >= days[-1]: # days 비어있으면 days[-1 ] 찾을 시 오류남
            days.pop()  # [9]
            func += 1 # func = 2
        answer.append(func)
    return answer