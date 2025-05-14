def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 입력 예시
# 7
# 1 2 3 4 5 6 7
# 4
n = int(input("배열 길이 (정렬된 상태): "))
arr = list(map(int, input("배열 요소들 (공백구분): ").split()))
target = int(input("찾을 값: "))

result = binary_search(arr, target)
print("결과:", result)
