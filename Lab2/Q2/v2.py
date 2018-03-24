import sys

def getSSE(lst):
    s = sum(lst)
    mean = s / len(lst)

    res = 0

    for i in lst:
        res += (i - mean) ** 2

    return res

def v_opt_dp(x, b):
    matrix = [[-1] * len(x) for _ in range(b)]
    matrixPath = [[None] * len(x) for _ in range(b)]
    
    rightmost = len(x) - 1

    res = []
    #print(rightmost)
    
    for i in range(b):
        for j in range(rightmost - i, rightmost - i - b + 1, -1):

            if j == rightmost - i:
                matrix[i][j] = 0

                temp_l = []
                for jj in range(j, rightmost + 1):
                    temp_l += [x[jj]]

                matrixPath[i][j] = temp_l
                continue

            if i + 1 == 1:
                matrix[i][j] = getSSE(x[j:])
                matrixPath[i][j] = [x[j:]]
                continue

           
            splitNb = i + 1
            k = j
            kMax = rightmost - i
            targetK = j;
           
            minValue = float('inf')

            
            for kk in range(k, kMax + 1):

                currValue = getSSE(x[j: kk + 1]) + matrix[i - 1][kk + 1]
                
                if(minValue > currValue):
                    targetK = kk
                    minValue = currValue


            matrix[i][j] = minValue
            matrixPath[i][j] = [x[j: targetK + 1]] + matrixPath[i - 1][targetK + 1]
            
            
            


    return matrix, matrixPath[b - 1][0]
                


