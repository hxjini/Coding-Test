import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [input().strip() for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

q = deque([(0, 0, 1)])
visited[0][0] = True

while q:
    x, y, dist = q.popleft()

    if x == n-1 and y == m-1:
        print(dist)
        break

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if maze[nx][ny] == '1' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))