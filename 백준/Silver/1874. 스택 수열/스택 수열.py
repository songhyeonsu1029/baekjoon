import sys

input = sys.stdin.read
lines = input().splitlines()
n = int(lines[0])
data = list(map(int, lines[1:]))

stack = []  # 스택 초기화
result = []  # 연산 기록
current = 1  # 스택에 추가할 숫자 시작 값
valid = True  # 수열 생성 가능 여부

for num in data:
    while current <= num:  # 현재 숫자까지 스택에 추가
        stack.append(current)
        result.append("+")
        current += 1

    if stack and stack[-1] == num:  # 스택의 최상단 숫자가 현재 숫자와 같으면 팝
        stack.pop()
        result.append("-")
    else:  # 수열을 만들 수 없는 경우
        valid = False
        break

if valid:
    print("\n".join(result))
else:
    print("NO")
