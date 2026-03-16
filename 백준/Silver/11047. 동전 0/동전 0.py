import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted(int(input()) for _ in range(n))

ans = 0
for i in range(n - 1, -1, -1):
    ans += (k//coins[i])
    k %= coins[i]
    
    
print(ans)
