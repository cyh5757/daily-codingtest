def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # 이번 턴에 교환이 발생했는가?
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # 정렬 완료 상태
            break

## 원래 버블 정렬
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):  # 마지막 i개는 이미 정렬됨
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
