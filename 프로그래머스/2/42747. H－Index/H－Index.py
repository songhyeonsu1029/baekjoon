#  [6,5,2,1,0] -> len(citations) - i >= citations[i] 

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for i in range(len(citations)): # citations[i] 번 이상 인용된 논문이 (i+1)개 있는 상태
        if citations[i] >= i+1:
            answer = i+1
            
    return answer