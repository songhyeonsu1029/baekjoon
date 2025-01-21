import sys

n = int(sys.stdin.readline().strip())

# 초기화
S = set()

# 명령 처리
for _ in range(n):
    command = sys.stdin.readline().strip()
    if command == "all":
        S = set(range(1, 21))
    elif command == "empty":
        S = set()
    else:
        cmd, num = command.split()
        num = int(num)

        if cmd == "add":
            S.add(num)
        elif cmd == "remove":
            S.discard(num)
        elif cmd == "check":
            print(1 if num in S else 0)
        elif cmd == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
