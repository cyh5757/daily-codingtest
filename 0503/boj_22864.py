A, B, C, M = map(int, input().split())

fatigue = 0  # 현재 피로도
work = 0     # 총 작업량

for _ in range(24):  # 하루는 24시간
    if fatigue + A <= M:
        fatigue += A
        work += B
    else:
        fatigue -= C
        if fatigue < 0:
            fatigue = 0

print(work)
