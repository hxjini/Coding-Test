INF = float('inf')

n = int(input())

ans = INF

for three in range(n//3 + 1): #(0, n//3 + 1)과 같음
    for five in range(n//5 + 1):
        if 3 * three + 5 * five == n: # if 3 * three + 5 * five == n and three + five < ans:
            ans = min(ans, three + five) # ans = three + five
            
if ans == INF: print(-1)
else: print(ans)
#print(-1 if ans == INF else ans)
            