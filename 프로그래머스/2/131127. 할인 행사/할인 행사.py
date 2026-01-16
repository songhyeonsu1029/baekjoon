
# def solution(want, number, discount):
#     answer = 0
#     dic = {}
#     for i in range(len(want)):
#         dic[want[i]] = number[i]
    
#     for i in range(len(discount)-9):
#         dic_discount = {}
#         for j in range(i, i+10):
#             if discount[j] in dic_discount:
#                 dic_discount[discount[j]] += 1
#             else:
#                 dic_discount[discount[j]] = 1
#         if dic_discount == dic:
#             answer += 1
            
#     return answer

from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    # 1. 원하는 품목과 개수를 딕셔너리 형태로 변환
    # 예: {'banana': 3, 'apple': 2, ...}
    target_dic = dict(zip(want, number))
    
    # 2. 할인 목록을 순회하며 10일치씩 잘라서 비교
    for i in range(len(discount) - 9):
        # i일부터 i+10일까지 자른 뒤, 개수를 셉니다.
        # Counter는 자동으로 리스트의 요소 개수를 딕셔너리 형태로 만들어줍니다.
        current_dic = Counter(discount[i : i+10]) 
        
        # 3. 비교 (Counter 객체나 딕셔너리는 == 연산자로 내용 비교 가능)
        if current_dic == target_dic:
            answer += 1
            
    return answer