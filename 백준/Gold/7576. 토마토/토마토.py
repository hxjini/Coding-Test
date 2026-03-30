import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            # 익은 토마토(1)의 좌표를 큐에 저장
            q.append((i, j))

dirs= [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                q.append((nx, ny))

ans = 1
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans, tomatoes[i][j])

print(ans-1)