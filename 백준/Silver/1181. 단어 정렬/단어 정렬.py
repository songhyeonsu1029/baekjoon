n = int(input())

ls = [str(input()) for i in range(n)]

set_ls = set(ls)
ls = list(set_ls)
ls.sort()
ls.sort(key = len)

for i in ls:
    print(i)