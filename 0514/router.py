

import sys

input = sys.stdin.readline
N, C = map(int, input().split())
houses = sorted(int(input()) for _ in range(N))

left = 1  # 최소 거리
right = houses[-1] - houses[0]  # 최대 거리
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = 1
    last_installed = houses[0]

    for i in range(1, N):
        if houses[i] - last_installed >= mid:
            count += 1
            last_installed = houses[i]

    if count >= C:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)