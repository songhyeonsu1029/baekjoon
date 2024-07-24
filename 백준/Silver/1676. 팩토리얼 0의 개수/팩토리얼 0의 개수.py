n = int(input())
fact = 1
count = 0
for i in range(n):
    fact *= (i+1)

fct = str(fact)

for i in range(n):
    if(fct[-i-1] == '0'):
        count += 1
    else:
        break
print(count)    