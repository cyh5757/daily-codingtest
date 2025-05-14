#https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def solution(numbers, target):
    def dfs(index, total):
        if index == len(numbers):
            return 1 if total == target else 0
        # 두 가지 경우로 재귀 호출
        return dfs(index + 1, total + numbers[index]) + dfs(index + 1, total - numbers[index])
    
    return dfs(0, 0)


