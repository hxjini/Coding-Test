import sys
input = sys.stdin.readline

n = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_price = float('inf') #가장 큰 값
ans = 0
for i in range(n - 1):
    min_price = min(min_price, costs[i])
    ans += min_price * dists[i]

print(ans)

