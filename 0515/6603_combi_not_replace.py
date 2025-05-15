from itertools import combinations
import sys

input = sys.stdin.readline

while True:
    line = input().strip()
    if line == '0':
        break
    nums = list(map(int, line.split()))
    k = nums[0]
    s = nums[1:]
    
    for comb in combinations(s, 6):  
        print(' '.join(map(str, comb)))
    print()
