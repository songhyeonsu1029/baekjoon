n, m = map(int, input().split())
board = [input() for _ in range(n)]
count = []

for a in range(n-7):
    for b in range(m-7):
        w_index = 0 #시작이 w -> 짝수칸 w 홀수칸 b (wbwbwb)
        b_index = 0 #시작이 b -> 짝수칸 b 홀수칸 w (bwbwbw)
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W': # 짝수칸이 b일때
                        w_index += 1 # 시작이 w인 패턴 1증가
                    if board[i][j] != 'B': # 짝수칸이 w일때
                        b_index += 1
                else:
                    if board[i][j] != 'W': #홀수칸이 b일때
                        b_index += 1 #시작이 b인 패턴 1증가
                    if board[i][j] != 'B': #홀수칸이 w일때
                        w_index += 1
        count.append(min(w_index, b_index))
        
print(min(count))
                