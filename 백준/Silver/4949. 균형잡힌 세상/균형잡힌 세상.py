def is_blanced(string):
    stack = []
    for i in string:
        if i in "([":
            stack.append(i)
        elif i == "]":
            if not stack or stack[-1] != "[":
                return "no"
            stack.pop()
        elif i == ")":
            if not stack or stack[-1] != "(":
                return "no"
            stack.pop()
    return "yes" if not stack else "no"
            
        
while True:
    line = input()
    if line == '.':
        break
    print(is_blanced(line))