import sys
input = sys.stdin.read

data = input().split()

n = int(data[0])

numbers = list(map(int, data[1:]))
    
numbers.sort()
for number in numbers:
    print(number)