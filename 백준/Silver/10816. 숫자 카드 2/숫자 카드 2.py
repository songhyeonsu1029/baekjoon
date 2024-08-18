n = int(input())
card1 = list(map(int, input().split()))
m = int(input())
card2 = list(map(int, input().split()))

count = {}
for card in card1:
    if card in count:
        count[card] +=1
    else:
        count[card] = 1
        
result = []
for card in card2:
    if card in count:
        result.append(count[card])
    else:
        result.append(0)
        
print(' '.join(map(str, result)))    