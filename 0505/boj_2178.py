from collections import deque

# N: 행 개수, M: 열 개수 입력받기
N, M = map(int, input().split())

# 미로 정보 저장 (문자열 리스트)
A = []
for _ in range(N):
    A.append(input())
    # 미로의 시작 위치는 (0,0), 도착 위치는 (N-1,M-1)

# 방문 여부를 저장하는 2차원 리스트
visit = [[False] * M for _ in range(N)]

# 시작 지점에서의 최단 거리 저장 리스트 (초기값 -1)
dist = [[-1]*M for _ in range(N)]

# BFS를 위한 큐 선언 및 시작 위치 삽입
queue = deque([(0, 0)])
visit[0][0] = True        # 시작 위치 방문 처리
dist[0][0] = 0            # 시작 위치 거리 0

# BFS 수행
while len(queue) != 0:
    r, c = queue.popleft()  # 현재 위치 좌표

    # 위쪽 이동
    if r > 0 and A[r-1][c] == '1' and not visit[r-1][c]:
        queue.append((r-1, c))
        visit[r-1][c] = True
        dist[r-1][c] = dist[r][c] + 1

    # 아래쪽 이동
    if r < N-1 and A[r+1][c] == '1' and not visit[r+1][c]:
        queue.append((r+1, c))
        visit[r+1][c] = True
        dist[r+1][c] = dist[r][c] + 1

    # 왼쪽 이동
    if c > 0 and A[r][c-1] == '1' and not visit[r][c-1]:
        queue.append((r, c-1))
        visit[r][c-1] = True
        dist[r][c-1] = dist[r][c] + 1

    # 오른쪽 이동
    if c < M-1 and A[r][c+1] == '1' and not visit[r][c+1]:
        queue.append((r, c+1))
        visit[r][c+1] = True
        dist[r][c+1] = dist[r][c] + 1

# 도착지점까지의 거리 출력 (시작점 포함이므로 +1)
print(dist[N-1][M-1] + 1)
