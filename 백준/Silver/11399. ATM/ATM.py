n = int(input().rstrip())

arr = list(map(int, input().split()))

arr.sort()

nesting = 0
for i in range(n):
    arr[i] += nesting
    nesting = arr[i]


print(sum(arr))
