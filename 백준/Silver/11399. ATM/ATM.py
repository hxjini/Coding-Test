import sys
input = sys.stdin.readline

n = int(input())
times = sorted(list(map(int, input().split())))

total = 0
for i in range(n):
    numsum = 0
    for j in range(0, i+1):
        numsum += times[j]
    total += numsum

print(total)