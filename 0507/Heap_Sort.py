import heapq

def heap_sort_ascending(arr):
    min_heap = []

    # 1. 배열을 힙에 넣기
    for num in arr:
        heapq.heappush(min_heap, num)

    sorted_arr = []
    # 2. 가장 작은 값을 하나씩 꺼내서 정렬
    while min_heap:
        sorted_arr.append(heapq.heappop(min_heap))

    return sorted_arr

# 사용자 입력
# 예: 5 2 9 1
arr = list(map(int, input().split()))
sorted_arr = heap_sort_ascending(arr)
print("오름차순 정렬 결과:", sorted_arr)
