def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 입력 예시
# 5
# 4 2 5 1 3
# 5
n = int(input("배열 길이: "))
arr = list(map(int, input("배열 요소들 (공백구분): ").split()))
target = int(input("찾을 값: "))

result = linear_search(arr, target)
print("결과:", result)
