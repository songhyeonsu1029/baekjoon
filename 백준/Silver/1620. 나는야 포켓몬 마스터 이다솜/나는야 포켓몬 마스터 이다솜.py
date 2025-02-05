import sys

input = sys.stdin.readline

a, b = map(int, input().split())

dict = {}
for i in range(1, a+1):
    pokemon = input().rstrip()
    dict[i] = pokemon
    dict[pokemon] = i

for _ in range(b):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])