# def solution(s):
#     stack = []
#     for i in s:
#         if i == '(':
#             stack.append(i)
#         else:
#             if len(stack) == 0:
#                 return False
#             stack.pop(-1)
#     return len(stack) == 0


def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0