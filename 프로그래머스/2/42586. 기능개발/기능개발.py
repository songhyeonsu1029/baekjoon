# progress, speeds 배열로 개발이 완료되는 시점인 times 배열 생성
# times 배열을 순차적으로 돌면서 더 큰 수가 나올때까지 count
# 각 count를 answer에 append

def solution(progresses, speeds):
    answer = []
    times = []
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            times.append((100 - progresses[i]) // speeds[i])
        else :
            times.append(((100 - progresses[i]) // speeds[i]) + 1)
    
    max_index = 0
    count = 1
    for i in range(len(times) - 1):
        if times[max_index] >= times[i+1]:
            count += 1
        else:
            max_index = i+1
            answer.append(count)
            count = 1
            
    answer.append(count)
    return answer