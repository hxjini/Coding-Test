import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted(list(int(input()) for _ in range(n)), reverse = True) 

ans = 0
for coin in coins:
    ans += (k//coin)
    k %= coin
    
    if k == 0:
        break
    
print(ans)
