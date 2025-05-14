# 버전
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
H = list(map(int, input().split()))

low, high = 0, max(H)
answer = 0

while low <= high:
    mid = (low + high) // 2
    total = sum(h - mid for h in H if h > mid)  

    if total >= M:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
