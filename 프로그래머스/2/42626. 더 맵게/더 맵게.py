import heapq

def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    count = 0
    
    while heap[0] < K:
        if len(heap) < 2:   
            return -1
        count+=1
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        ex = first + (second * 2)
        heapq.heappush(heap, ex)
    return count