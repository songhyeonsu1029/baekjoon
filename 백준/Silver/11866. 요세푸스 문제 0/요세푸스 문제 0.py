n, k = map(int, input().split())

idx = 0
queue = [i for i in range(1, n+1)]
result = []
while queue:
    idx += k-1
    if idx >= len(queue):
        idx %= len(queue)
    result.append(str(queue.pop(idx)))


print("<" + ", ".join(map(str, result)) + ">")    