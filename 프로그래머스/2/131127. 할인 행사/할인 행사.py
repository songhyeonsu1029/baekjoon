
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
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1

    return answer