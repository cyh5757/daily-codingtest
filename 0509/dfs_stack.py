#https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def solution(numbers, target):
    stack = [(0, 0)]  # (index, total)
    count = 0

    while stack:
        index, total = stack.pop()
        if index == len(numbers):
            if total == target:
                count += 1
        else:
            stack.append((index + 1, total + numbers[index]))
            stack.append((index + 1, total - numbers[index]))

    return count


