#https://www.acmicpc.net/problem/15649

from itertools import permutations

N, M = map(int, input().split())

for p in permutations(range(1, N + 1), M):
    print(' '.join(map(str, p)))


