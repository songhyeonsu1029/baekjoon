import sys

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

input = sys.stdin.read

data = input().splitlines()
n = int(data[0])
scores = list(map(int, data[1:]))

if n == 0:
    print(0)
else:
    scores.sort()
    cut = roundUp(n*0.15)
    new_scores = scores[cut : n - cut]
    new_scores_mean = roundUp(sum(new_scores) / len(new_scores))
    print(new_scores_mean)