# # 최적화된 버전
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# H = list(map(int, input().split()))

# low, high = 0, max(H)
# answer = 0

# while low <= high:
#     mid = (low + high) // 2
#     total = sum(h - mid for h in H if h > mid)  # 리스트 컴프리헨션으로 최적화

#     if total >= M:
#         answer = mid
#         low = mid + 1
#     else:
#         high = mid - 1

# print(answer)

import sys
import bisect
from itertools import accumulate

input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
H = list(map(int, input().split()))

# 나무 높이 정렬
H.sort()

# 누적합 배열 생성 (accumulate는 반환이 iterator라 list로 감싸줌)
prefix_sum = list(accumulate(H))

low, high = 0, H[-1]
answer = 0

while low <= high:
    mid = (low + high) // 2

    # mid보다 큰 나무의 첫 인덱스 찾기
    idx = bisect.bisect_right(H, mid)

    # 남은 나무들의 개수
    count = N - idx

    # 자를 수 있는 총 길이 = 전체 높이 합 - mid * 남은 나무 수
    if count > 0:
        total = prefix_sum[-1] - (prefix_sum[idx - 1] if idx > 0 else 0)
        cut = total - mid * count
    else:
        cut = 0

    if cut >= M:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
