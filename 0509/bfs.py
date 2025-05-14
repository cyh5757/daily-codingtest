#https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3
from collections import deque

def can_convert(word1, word2):
    # 두 단어가 한 글자만 다르면 True
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
    return count == 1

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append((begin, 0))  # (현재 단어, 변환 횟수)

    while queue:
        current, count = queue.popleft()
        if current == target:
            return count

        for word in words:
            if can_convert(current, word):
                queue.append((word, count + 1))
                words.remove(word)  # 중복 탐색 방지

    return 0
