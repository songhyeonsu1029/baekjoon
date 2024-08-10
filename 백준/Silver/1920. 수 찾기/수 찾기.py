def binary_search(arr, target):
    left, right = 0, len(arr)-1
    
    while left<=right:
        mid = (left + right)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else :
            right = mid-1
            
    return False

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

result = []
for i in b:
    if binary_search(a, i):
        result.append(1)
    else:
        result.append(0)
        
print("\n".join(map(str, result)))