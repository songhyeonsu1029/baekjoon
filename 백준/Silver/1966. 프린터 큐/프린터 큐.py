t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    #테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과
    #몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
    data = list(map(int, input().split()))
    
    result = 1
    while data:
        if data[0] < max(data):
            data.append(data.pop(0))
        
        else:
            if m == 0: break
            
            data.pop(0)
            result += 1
            
        if m > 0:
            m = m-1
        else:
            m = len(data) - 1
            
    print(result)