def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ✅ 사용자 입력 받기
# 예: 5, 2, 9, 1
arr = list(map(int, input().split()))

sorted_arr = merge_sort(arr)
print("정렬 결과:", sorted_arr)


    #              [5, 2, 9, 1]
    #           /                 \
    #      [5, 2]              [9, 1]
    #     /      \            /      \
    #   [5]     [2]       [9]     [1]
    #     \      /            \      /
    #     [2, 5]              [1, 9]
    #           \            /
    #        [1, 2, 5, 9] ← 최종 결과
