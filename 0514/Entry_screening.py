def solution(n, times):
    left = 1
    right = max(times) * n  # 최악의 경우: 가장 느린 심사관이 모든 사람 처리

    answer = right
    while left <= right:
        mid = (left + right) // 2
        # mid 시간 동안 n명 이상 심사 가능한가?
        total = sum(mid // time for time in times)

        if total >= n:
            answer = mid  # 가능한 최소 시간 저장
            right = mid - 1  # 더 짧은 시간 시도
        else:
            left = mid + 1  # 시간 더 필요

    return answer