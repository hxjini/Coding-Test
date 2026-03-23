import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = list(input().strip() for _ in range(n))

ans = 64

for i in range(0, n - 7):
    for j in range(0, m - 7): # 0 생략 가능

        case1 = 0
        case2 = 0
        
        for x in range(i, i + 8): # 8번 실행
            for y in range(j, j + 8): #  x, y 총 64번 실행(8X8) 총 시간 복잡도 = 64(m-7)(n-7)
                if(x + y) % 2 == 1:
                    if board[x][y] == 'B': case1 += 1
                    if board[x][y] == 'W': case2 += 1
                else: # (x + y) % 2 == 0
                    if board[x][y] == 'W': case1 += 1
                    if board[x][y] == 'B': case2 += 1
        ans = min(ans, case1, case2)
print(ans)