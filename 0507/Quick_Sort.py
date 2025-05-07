def quick_sort(arr):
    # 리스트가 하나 이하일 경우 그대로 반환
    if len(arr) <= 1:
        return arr

    # 피벗 설정 (여기서는 첫 번째 요소)
    pivot = arr[0]
    tail = arr[1:]

    # 피벗보다 작은 값과 큰 값 나누기
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    # 재귀 호출 후 합치기
    return quick_sort(left) + [pivot] + quick_sort(right)

# 사용자 입력
# 예: 5 2 9 1
arr = list(map(int, input().split()))
sorted_arr = quick_sort(arr)
print("정렬 결과:", sorted_arr)


        #             [5, 2, 9, 1]
        #              pivot = 5
        #             /         \
        #     [2, 1]             [9]
        #     pivot = 2
        #    /     \
        # [1]      []
