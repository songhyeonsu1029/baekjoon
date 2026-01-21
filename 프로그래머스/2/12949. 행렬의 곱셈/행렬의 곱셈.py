# arr1[1][1]*arr2[1][1] + arr[1][2] * arr[2][1] = answer[1][1]
# arr1[i][j]*arr2[j][i] + arr[]

def solution(arr1, arr2):
    answer = []
    m, n, r = len(arr1), len(arr1[0]), len(arr2[0])
    
    for i in range(m):
        arr = arr1[i]
        result = []
        for j in range(r):
            sum = 0
            for k in range(n):
                sum += arr[k]*arr2[k][j]
            result.append(sum)
        answer.append(result)
    
    return answer