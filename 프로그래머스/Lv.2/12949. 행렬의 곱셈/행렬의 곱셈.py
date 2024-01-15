def solution(arr1, arr2):
    ans = [[0]*len(arr2[1]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[1])):
            row = arr1[i]
            col = [row2[j] for row2 in arr2]
            tmp = 0
            for k,l in zip(row,col):
                tmp += k*l
            ans[i][j] = tmp
    return ans