N = int(input())         # 사용자로부터 정수 N을 입력받음
low = 0                  # 이진 탐색의 하한: 0부터 시작
high = N                 # 이진 탐색의 상한: N (제곱근은 N 이상일 수 없음)
ans = -1                 # 정답 변수 초기화

while low <= high:
    mid = (low + high) // 2   # 중간값 계산 (현재 후보 제곱근)

    if mid * mid < N:
        # mid^2이 N보다 작다면 제곱근이 더 큼 → 오른쪽 탐색
        low = mid + 1
    else:
        # mid^2이 N보다 크거나 같다면, mid는 정답 후보
        # 더 작은 제곱근이 있을 수 있으므로 왼쪽을 계속 탐색
        ans = mid
        high = mid - 1

# 최종적으로 ans는 N보다 크거나 같은 최소의 정수 제곱근 (⌈√N⌉)
print(ans)