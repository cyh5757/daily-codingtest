#https://www.acmicpc.net/problem/15650

from itertools import combinations

N, M = map(int, input().split())

for comb in combinations(range(1, N + 1), M):
    print(' '.join(map(str, comb)))