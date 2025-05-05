#큐

from collections import deque

N, K = map(int, input().split())

queue = deque()
for i in range(K, N+1):
    #(K,K+1,..,N-2,N-1,N)
    queue.append(i)
for i in range(1,K):
    #(K,K+1,..,N-2,N-1,N) +(1,2,3,K-1)
    # 원형 큐 초기화
    queue.append(i)
     
answer = []
while True:
    answer.append(queue.popleft())

    if len(queue) ==0:
        break


    # K번쨰들만큼 이동
    for _ in range(K-1):
        u = queue.popleft()
        queue.append(u)

print("<",end="")
for i in range(N-1):
    print(answer[i], end= ", ")
print(answer[N-1],end = ">")    

