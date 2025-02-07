import sys

input = sys.stdin.readline

n, k = map(int, input().split())

list = []
for _ in range(n):
    coin = int(input().rstrip())
    list.append(coin)

list.sort(reverse=True)

min = 0
for i in list:
    if i <= k:
        min += k//i
        k = k%i
        if k == 0:
            break

print(min)