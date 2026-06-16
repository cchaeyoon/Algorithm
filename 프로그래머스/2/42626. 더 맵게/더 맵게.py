import heapq

def solution(scoville, K):
    answer = -1
    heapq.heapify(scoville)
    
    freq = 0
    while scoville[0] < K and len(scoville) != 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        freq += 1
        
    if len(scoville) == 1 and scoville[0] < K:
        answer = -1
    else:
        answer = freq
        
    return answer