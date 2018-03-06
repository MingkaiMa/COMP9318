def nsqrt(n):
    if n < 0:
        return None

    if n == 0 or n == 1:
        return n


    left = 1
    right = n

    result = None
    
    while(left <= right):
        middle = (left + right) // 2
        
        sqMiddle = middle * middle
        
        if sqMiddle == n:
            return middle

        if sqMiddle < n:
            result = middle

            left = middle + 1

        else:
            right = middle - 1


    return result


if __name__ == '__main__':
    L = []
    for i in range(1, 1000000):
        L.append(nsqrt(i))

    print(L)
        

            
    
    
