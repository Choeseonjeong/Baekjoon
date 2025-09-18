import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    count = 0
    while heap and heap[0] < K and len(heap) >= 2:
        heapq.heappush(heap,heapq.heappop(heap)+heapq.heappop(heap)*2)
        count += 1
    return count if heap and heap[0] >= K else -1