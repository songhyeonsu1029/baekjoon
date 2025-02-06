import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = set()
for i in range(n):
    name = input().rstrip()
    a.add(name)
    
b = set()
for _ in range(m):
    name = input().rstrip()
    b.add(name)

c = a & b

print(len(c))
for item in sorted(c):
    print(item)

    